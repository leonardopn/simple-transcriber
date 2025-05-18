from helper.audio_converter import AudioConverter
from helper.transcriber import Transcriber


def main():
    try:
        print("")
        file_path = AudioConverter().m4a_to_wav()

        print("")
        Transcriber().transcribe_audio(
            audio_path=file_path, model_name="large", language="pt"
        )
        print("")
    except KeyboardInterrupt:
        print("Process interrupted by user.")


if __name__ == "__main__":
    main()
