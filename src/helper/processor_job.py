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

    def start(self):
        try:
            input_dir = os.path.join(PROJECT_DIR, "temp", "input")
            output_dir = os.path.join(PROJECT_DIR, "temp", "output")

            self.clearOutputDir()
            os.makedirs(input_dir, exist_ok=True)
            os.makedirs(output_dir, exist_ok=True)

            print("Starting processor job...")

            for filename in os.listdir(input_dir):
                converted_wav_file_path = os.path.join(input_dir, filename)
                if os.path.isfile(converted_wav_file_path):
                    folder_name = f"{output_dir}/{filename}"
                    os.makedirs(folder_name, exist_ok=True)

                    output_filename = f"{folder_name}/audio.wav"

                    print("")
                    converted_wav_file_path = AudioConverter().m4a_to_wav(
                        input_file_path=converted_wav_file_path,
                        output_file_path=output_filename,
                    )

                    print("")
                    Transcriber().transcribe_audio(
                        audio_path=converted_wav_file_path,
                        model_name="large",
                        language="pt",
                    )
                    print("")

        except KeyboardInterrupt:
            print("Process interrupted by user.")
