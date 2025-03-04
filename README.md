# flask-webui
Very simple WebUI for running on a Flask server to chat with an Ollama server

This is a very simple and light Web UI for chatting with an Ollama server.

**Features:**
1. Simple SMS-like chat function using an Ollama server and an Apache Tika Server.
2. Upload files or Drag & Drop for processing to add context to a conversation.
3. Customizable for services either local or running on another server.
4. Passes Date and Time to the LLM from server.
5. The Tika server will process the following document types:
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

