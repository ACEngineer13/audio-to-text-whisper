import os
import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import whisper

class WhisperApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Whisper Transcription")
        self.geometry("400x200")

        self.drop_label = tk.Label(self, text="Drag and drop an audio file here", relief="ridge", width=40, height=4)
        self.drop_label.pack(pady=20)
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.on_drop)

        self.file_path = None

        self.start_btn = tk.Button(self, text="Start", command=self.transcribe)
        self.start_btn.pack(pady=10)

    def on_drop(self, event):
        # event.data may contain surrounding braces when multiple files are dropped
        path = event.data
        if path.startswith('{') and path.endswith('}'):
            path = path[1:-1]
        self.file_path = path
        self.drop_label.config(text=os.path.basename(path))

    def transcribe(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please drop an audio file first")
            return
        self.start_btn.config(state='disabled')
        self.update()
        try:
            model = whisper.load_model("base")
            result = model.transcribe(self.file_path)
            out_path = os.path.splitext(self.file_path)[0] + '.txt'
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(result['text'])
            messagebox.showinfo("Done", f"Transcription saved to {out_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.start_btn.config(state='normal')

if __name__ == '__main__':
    app = WhisperApp()
    app.mainloop()
