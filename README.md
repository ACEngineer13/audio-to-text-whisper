# audio-to-text-whisper

A simple GUI app to transcribe audio files to text using OpenAI's Whisper.

## Usage

1. Install the dependencies:
   ```bash
   pip install openai-whisper tkinterdnd2
   ```

2. Run the application:
   ```bash
   python app.py
   ```

   Drag and drop an audio file onto the window and click **Start** to create a `.txt` transcription next to the audio file.

## Building a Windows executable

If you want a standalone `.exe` file, install `pyinstaller` and build the app:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole app.py
```

The executable will be available in the `dist` folder.
