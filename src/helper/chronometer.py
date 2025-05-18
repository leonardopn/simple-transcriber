from time import time


class Chronometer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.end_time = None
        self.start_time = time()

    def stop(self):
        if self.start_time is None:
            raise ValueError("Chronometer has not been started.")
        self.end_time = time()

    def elapsed_time(self, human_readable: bool = False) -> str:
        if self.start_time is None or self.end_time is None:
            raise ValueError("Chronometer has not been started and stopped properly.")
        result = self.end_time - self.start_time

        self.start_time = None
        self.end_time = None

        if human_readable:
            minutes, seconds = divmod(result, 60)
            hours, minutes = divmod(minutes, 60)
            result = f"{int(hours)}:{int(minutes):02}:{int(seconds):02}"

        return str(result)
