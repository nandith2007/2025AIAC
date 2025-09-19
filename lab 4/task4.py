import csv

# Zero-shot Prompting
def analyze_csv_zero_shot(file_path):
    """
    Reads a CSV file and returns:
    - total number of rows
    - number of empty rows
    - total number of words across the file
    """
    total_rows = 0
    empty_rows = 0
    word_count = 0
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            word_count += sum(len(cell.split()) for cell in row)
    return total_rows, empty_rows, word_count

# One-shot Prompting (with example)
def analyze_csv_one_shot(file_path):
    """
    Example: For a CSV with rows:
    a,b,c
    ,,
    hello world,foo,bar
    Returns: (3, 1, 6)
    """
    total_rows = 0
    empty_rows = 0
    word_count = 0
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            for cell in row:
                word_count += len(cell.split())
    return total_rows, empty_rows, word_count

# Few-shot Prompting (with multiple examples)
def analyze_csv_few_shot(file_path):
    """
    Example 1: CSV rows:
    a,b
    ,,
    Returns: (2, 1, 2)
    Example 2: CSV rows:
    hello,world
    foo,bar
    Returns: (2, 0, 4)
    """
    total_rows = 0
    empty_rows = 0
    word_count = 0
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            for cell in row:
                word_count += len(cell.split())
    return total_rows, empty_rows, word_count

if __name__ == "__main__":
    print("Choose prompting style:")
    print("1. Zero-shot")
    print("2. One-shot")
    print("3. Few-shot")
    choice = input("Enter 1, 2, or 3: ").strip()
    file_path = input("Enter path to CSV file: ").strip()

    if choice == "1":
        result = analyze_csv_zero_shot(file_path)
    elif choice == "2":
        result = analyze_csv_one_shot(file_path)
    elif choice == "3":
        result = analyze_csv_few_shot(file_path)
    else:
        print("Invalid choice.")
        exit(1)

    print(f"Total rows: {result[0]}")
    print(f"Empty rows: {result[1]}")
    print(f"Total words: {result[2]}")
    