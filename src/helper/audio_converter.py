from ffmpeg import FFmpeg
from datetime import datetime


class AudioConverter:
    def m4a_to_wav(self) -> str:
        print("Converting m4a to wav...")

        now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        output_filename = f"temp/{now}.wav"

        FFmpeg().input("audio.m4a").output(output_filename, ar=16000, ac=1).execute()

        print("Conversion complete. Output saved to:", output_filename)
        return output_filename
