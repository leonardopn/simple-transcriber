import os
from typing import Literal
import whisper
from helper.chronometer import Chronometer

Model = Literal["tiny", "base", "small", "medium", "large", "turbo"]
Language = Literal["en", "pt"]


class Transcriber:

    def transcribe_audio(
        self, audio_path: str, model_name: Model, language: Language
    ) -> str:
        """Transcreve o áudio usando Whisper."""

        chronometer = Chronometer()
        chronometer.start()

        print("Loading whisper model...")
        model = whisper.load_model(model_name)
        print("Model loaded.")

        print("Transcribing audio...")
        result = model.transcribe(audio_path, language=language)

        parent_path = os.path.dirname(audio_path)
        output_file = os.path.join(parent_path, "transcription.txt")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])

        chronometer.stop()
        elapsed_time = chronometer.elapsed_time(True)
        print(
            f"[{elapsed_time}] - Transcription complete. Output saved to:", output_file
        )

        return result["text"]
