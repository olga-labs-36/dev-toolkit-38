import json
from validators import validate_input

class MainProcessor:
    def __init__(self):
        self.data = []

    def main_loop(self):
        while True:
            user_input = input('Enter data (or type exit to quit): ')
            if user_input.lower() == 'exit':
                break
            if not validate_input(user_input):
                print('Invalid input. Please try again.')
                continue
            self.process_data(user_input)

    def process_data(self, data):
        self.data.append(data)
        print(f'Data processed: {data}')

if __name__ == '__main__':
    processor = MainProcessor()
    processor.main_loop()