from flask import Flask, render_template, request, jsonify
import requests
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

OLLAMA_API_URL = "http://192.168.0.211:11434/api/chat"
TIKA_API_URL = "http://192.168.0.211:9998/tika"
MODEL_NAME = "codellama"

# GPU and model configurations
MODEL_CONFIG = {
    "temperature": 0.5,
    "top_k": 40,
    "top_p": 0.9,
    "num_ctx": 4096,
    "num_gpu": 1,
    "num_thread": 56,
    "gpu_layers": 80
}

# Store conversation and document data
conversation_store = {
    'document': '',
    'messages': []
}

@app.route('/')
def index():
    global conversation_store
    conversation_store['messages'] = []
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    global conversation_store
    conversation_store['messages'] = []
    return jsonify({'status': 'success', 'message': 'Conversation reset'})

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'files' not in request.files:
            return jsonify({'error': 'No files provided'}), 400
            
        files = request.files.getlist('files')
        if not files:
            return jsonify({'error': 'No files selected'}), 400

        extracted_texts = []
        for file in files:
            headers = {
                'Accept': 'text/plain',
                'Content-Type': file.content_type
            }
            
            logger.info(f"Sending file to Tika: {file.filename}")
            file_content = file.read()
            tika_response = requests.put(TIKA_API_URL, data=file_content, headers=headers)
            tika_response.raise_for_status()
            
            extracted_text = tika_response.text
            logger.info(f"Extracted text length: {len(extracted_text)}")
            logger.info(f"First 200 chars: {extracted_text[:200]}")
            
            if extracted_text.strip():
                extracted_texts.append(extracted_text)

        if not extracted_texts:
            return jsonify({'error': 'No text could be extracted from the documents'}), 400

        # Store document content
        conversation_store['document'] = "\n\n".join(extracted_texts)

        return jsonify({
            'message': 'Documents processed successfully',
            'status': 'success'
        })
        
    except Exception as e:
        logger.error(f"Error processing files: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({'error': 'No message provided'}), 400

        global conversation_store

        # Add user message to history
        conversation_store['messages'].append({
            "role": "user",
            "content": user_input
        })

        # Prepare system message with current date
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        system_message = f"""You are a helpful AI assistant. 
        The current date and time is {current_date}.
        Use markdown formatting in your responses.
        Format code blocks with appropriate syntax highlighting."""

        # Add document context if available
        if conversation_store.get('document'):
            system_message += f"\n\nUse this document as context:\n{conversation_store['document']}"

        # Prepare messages with context
        messages = [
            {
                "role": "system",
                "content": system_message
            }
        ] + conversation_store['messages']

        # Send to Ollama with GPU configuration
        ollama_payload = {
            "model": MODEL_NAME,
            "messages": messages,
            "stream": True,
            "options": MODEL_CONFIG
        }

        logger.info("Sending request to Ollama with GPU configuration")
        response = requests.post(OLLAMA_API_URL, json=ollama_payload, stream=True)
        response.raise_for_status()
        
        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    chunk = json.loads(line.decode('utf-8'))
                    if 'message' in chunk and 'content' in chunk['message']:
                        full_response += chunk['message']['content']
                except json.JSONDecodeError:
                    continue

        # Add response to history
        conversation_store['messages'].append({
            "role": "assistant",
            "content": full_response
        })

        return jsonify({
            'response': full_response,
            'conversation': conversation_store['messages']
        })
    
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/date', methods=['GET'])
def get_date():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({'date': current_date})

if __name__ == '__main__':
    app.run(debug=True)