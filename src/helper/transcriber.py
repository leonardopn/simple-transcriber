import os
from typing import Literal
from helper.chronometer import Chronometer
from faster_whisper import WhisperModel

Model = Literal["tiny", "base", "small", "medium", "large", "turbo"]
Language = Literal["en", "pt"]


class Transcriber:

    def transcribe_audio(self, audio_path: str, language: Language) -> str:
        """Transcreve o áudio usando Whisper."""

        chronometer = Chronometer()
        chronometer.start()

        print("Loading whisper model...")

        # Run on GPU with FP16
        model = WhisperModel("large-v3", device="cuda", compute_type="float16")

        print("Model loaded.")

        print("Transcribing audio...")
        segments, _ = model.transcribe(audio_path, language=language, beam_size=5)

        parent_path = os.path.dirname(audio_path)
        output_file = os.path.join(parent_path, "transcription.txt")

        result: str = ""
        for segment in segments:
            result += segment.text + "\n"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)

        chronometer.stop()
        elapsed_time = chronometer.elapsed_time(True)
        print(
            f"[{elapsed_time}] - Transcription complete. Output saved to:", output_file
        )

        return result
