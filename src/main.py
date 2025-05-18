from helper.audio_converter import AudioConverter

def main():
    try:
        AudioConverter().m4a_to_wav()
    except KeyboardInterrupt:
        print("Process interrupted by user.")

if __name__ == "__main__":
    main()
