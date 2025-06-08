import argparse
import whisper


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe audio to text using OpenAI Whisper"
    )
    parser.add_argument("audio_file", help="Path to the audio file")
    parser.add_argument(
        "output_file", help="Path to the file where the transcription will be saved"
    )
    parser.add_argument(
        "--model", default="base", help="Whisper model to use (default: base)"
    )
    args = parser.parse_args()

    model = whisper.load_model(args.model)
    result = model.transcribe(args.audio_file)

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(result["text"].strip())


if __name__ == "__main__":
    main()
