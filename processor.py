import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"{func.__name__} executed in {duration:.4f} seconds")
        return result
    return wrapper

@time_it
def process_data(data):
    result = []
    for item in data:
        processed_item = item ** 2  # Replace with actual processing
        result.append(processed_item)
    return result

@time_it
def batch_process(data_list, batch_size):
    results = []
    for i in range(0, len(data_list), batch_size):
        batch = data_list[i:i + batch_size]
        results.extend(process_data(batch))
    return results

if __name__ == '__main__':
    sample_data = range(10000)
    batch_results = batch_process(sample_data, 100)
    print(batch_results)