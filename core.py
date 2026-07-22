import time

class PerformanceMonitor:
    def __init__(self):
        self.start_time = None
    
    def start(self):
        self.start_time = time.time()
    
    def stop(self):
        if self.start_time is None:
            raise RuntimeError("PerformanceMonitor not started")
        elapsed_time = time.time() - self.start_time
        self.start_time = None
        return elapsed_time

class OptimizedProcessor:
    def __init__(self):
        self.monitor = PerformanceMonitor()
    
    def process_data(self, data):
        self.monitor.start()
        result = self._heavy_computation(data)
        elapsed = self.monitor.stop()
        print(f'Processing took {elapsed:.4f} seconds')
        return result
    
    def _heavy_computation(self, data):
        time.sleep(1)  # Simulated heavy computation
        return [x * 2 for x in data]

if __name__ == '__main__':
    processor = OptimizedProcessor()
    processor.process_data([1, 2, 3, 4, 5])
