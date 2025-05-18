from ffmpeg import FFmpeg
from datetime import datetime
import os
from helper.chronometer import Chronometer


class AudioConverter:
    def m4a_to_wav(self) -> str:
        print("")
        chronometer = Chronometer()
        chronometer.start()

        print("Converting m4a to wav...")

        now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        folder_name = f"temp/{now}"
        os.makedirs(folder_name, exist_ok=True)

        output_filename = f"{folder_name}/audio.wav"

        FFmpeg().input("audio.m4a").output(output_filename, ar=16000, ac=1).execute()

        chronometer.stop()
        elapsed_time = chronometer.elapsed_time(True)
        print(
            f"[{elapsed_time}] - Conversion complete. Output saved to:", output_filename
        )
        print("")
        return output_filename
