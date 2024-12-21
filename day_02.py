from typing import List, Optional


def is_ordered(seq):
    # Check increasing
    increasing = all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))
    if increasing:
        return True
    # Check decreasing
    decreasing = all(seq[i] > seq[i + 1] for i in range(len(seq) - 1))
    return decreasing


def is_continuous(numbers: List[int]) -> bool:
    if len(numbers) <= 1:
        return True

    for x, y in zip(numbers, numbers[1:]):
        if not (1 <= abs(y - x) <= 3):
            return False

    return True


def correct_report(numbers: List[int]) -> bool:
    return is_ordered(numbers) and is_continuous(numbers)


def is_safe(numbers: List[int]) -> bool:
    if correct_report(numbers):
        return True
    
    # Try removing each number
    print("numbers:", numbers)
    for i in range(len(numbers)):
        subset = numbers[:i] + numbers[i + 1:]
        print("subset:", subset, "correct_report:", correct_report(subset))
        if correct_report(subset):
            return True

    return False


def process_file(file_path: str) -> int:
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]
        safe_count = 0
        for line in lines:
            numbers = line.split(' ')
            numbers = list(map(int, numbers))
            safe = is_safe(numbers)
            safe_count += safe
        print(f"safe_count: {safe_count} out of {len(lines)}")
    return safe_count


if __name__ == "__main__":
    process_file('day-02.txt')
