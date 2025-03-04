# flask-webui
Very simple Python WebUI for running on a Flask server to chat with an Ollama server

This is a very simple and light Web UI for chatting with an Ollama server.

**Features:**
1. Easily customizable HTML interface.
2. Simple SMS-like chat function using an Ollama server and an Apache Tika Server.
3. Upload files or Drag & Drop for processing to add context to a conversation.
4. Customizable for services either local or running on another server.
5. Passes Date and Time to the LLM from server.
6. The Tika server will process the following document types:
   * PDFs: Tika Server can parse and extract metadata from PDF files, including text, images, and other embedded resources.
   * Microsoft Office documents: Tika Server can parse and extract metadata from Microsoft Word, Excel, and PowerPoint documents, including text, tables, and charts.
   * Text files: Tika Server can parse and extract metadata from plain text files, including HTML, XML, JSON, and other text-based formats.
   * Images: Tika Server can parse and extract metadata from images, including JPEG, PNG, GIF, and other image file formats.
   * Audio and video files: Tika Server can parse and extract metadata from audio and video files, including MP3, MP4, AVI, and other audio and video file formats.
   * Email messages: Tika Server can parse and extract metadata from email messages, including sender, recipient, subject, and body text.
   * Archives: Tika Server can parse and extract metadata from archives, including ZIP, RAR, and other archive file formats.
   * Web pages: Tika Server can parse and extract metadata from web pages, including HTML, XML, JSON, and other web page formats.
   * Documents: Tika Server can parse and extract metadata from documents, including Word, Excel, PowerPoint, and other document file formats.
   * Presentations: Tika Server can parse and extract metadata from presentations, including PowerPoint and other presentation file formats.

**Installation**
1. You will need to install both Ollama and Apache Tika server, easiest method is via docker containers.
2. Download the LLM modelfile that you wish to use (via Ollama)
3. Install Python. This has been tested on Python 3.11, but should work on other versions.
4. Create a directory and clone this repository.
5. Switch to the directory.
6. Customize the app.py file for the server locations, model name and any other parameters (or leave defaults).
7. Create and activate a python venv.
   * _python3.11 -m venv llmchat_
   * _source llmchat/bin/activate_
8. Upgrade pip : _pip install --upgrade pip_
9. Install Flask and Requests: _pip install flask requests_
10. From the directory where app.py resides run: _flask run --host=0.0.0.0 --port=5000_
11. Go to a browser and navigate to http://localhost:5000

**Notes:** 
1. This is NOT for production use without modifications. At a minimum a reverse proxy or similar must be used when exposing to an unsecure network.
2. If using from another computer ensure that you have opened tcp port 5000 on the server firewall.
3. You can customize the UI with an HTML editor. 
