from definitions import PROJECT_DIR
from helper.audio_converter import AudioConverter
from helper.transcriber import Transcriber
import os
import shutil


class ProcessorJob:
    def clearOutputDir(self):

        output_dir = os.path.join(PROJECT_DIR, "temp", "output")
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)

    def process_file(self, original_file_path: str, output_dir: str):
        file_name = os.path.basename(original_file_path)
        output_folder_path = f"{output_dir}/{file_name}"
        os.makedirs(output_folder_path, exist_ok=True)

        print("")
        converted_wav_file_path = AudioConverter().m4a_to_wav(
            input_file_path=original_file_path,
            output_file_path=f"{output_folder_path}/audio.wav",
        )

        print("")
        Transcriber().transcribe_audio(
            audio_path=converted_wav_file_path,
            language="pt",
        )

        print("")

    def start(self):
        try:
            input_dir = os.path.join(PROJECT_DIR, "temp", "input")
            output_dir = os.path.join(PROJECT_DIR, "temp", "output")

            self.clearOutputDir()
            os.makedirs(input_dir, exist_ok=True)
            os.makedirs(output_dir, exist_ok=True)

            print("Starting processor job...")

            for filename in os.listdir(input_dir):
                original_file_path = os.path.join(input_dir, filename)
                if os.path.isfile(original_file_path):
                    self.process_file(original_file_path, output_dir)

        except KeyboardInterrupt:
            print("Process interrupted by user.")
