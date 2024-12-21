from typing import List, Tuple
from collections import Counter


def parse_input(filename: str) -> Tuple[List[int], List[int]]:
    try:
        with open(filename, 'r') as file:
            numbers = [tuple(map(int, line.strip().split()))
                      for line in file if line.strip()]
        return zip(*numbers) if numbers else ([], [])
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return [], []
    except ValueError as e:
        print(f"Error parsing file: {e}")
        return [], []

def calculate_differences(first: List[int], second: List[int]) -> int:
    return sum(abs(x - y) for x, y in zip(first, second))

def calculate_similarities(first: List[int], second: List[int]) -> int:
    second_counter = Counter(second)
    return sum(num * second_counter[num] for num in first)

def main():
    first_numbers, second_numbers = parse_input('DAY-01.TXT')
    if not first_numbers or not second_numbers:
        return

    first_numbers = sorted(first_numbers)
    second_numbers = sorted(second_numbers)

    total_diff = calculate_differences(first_numbers, second_numbers)
    total_similarity = calculate_similarities(first_numbers, second_numbers)

    print(f"Total difference: {total_diff}")
    print(f"Total similarity: {total_similarity}")

if __name__ == "__main__":
    main()