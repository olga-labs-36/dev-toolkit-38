import time

class Performance:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()

    def elapsed_time(self):
        if self.start_time is None or self.end_time is None:
            raise ValueError('Timer has not been started or stopped.')
        return self.end_time - self.start_time

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        perf = Performance()
        perf.start()
        result = [x * x for x in self.data]
        perf.stop()
        print(f'Processing time: {perf.elapsed_time()} seconds')
        return result

if __name__ == '__main__':
    processor = DataProcessor(range(10000))
    processed_data = processor.process()