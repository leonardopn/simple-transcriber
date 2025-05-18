import ffmpeg
from helper.chronometer import Chronometer


class AudioConverter:
    def m4a_to_wav(self, input_file_path: str, output_file_path: str) -> str:
        chronometer = Chronometer()
        chronometer.start()

        print("Converting m4a to wav...")
        ffmpeg.input(input_file_path).output(output_file_path, ar=16000, ac=1).run(
            quiet=True
        )

        chronometer.stop()
        elapsed_time = chronometer.elapsed_time(True)
        print(
            f"[{elapsed_time}] - Conversion complete. Output saved to:",
            output_file_path,
        )

        return output_file_path
