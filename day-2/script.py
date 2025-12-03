def find_subtotal_invalid_ids_in_range(range_str):
    start_str, end_str = range_str.split("-")
    start, end = int(start_str), int(end_str)
    subtotal = 0
    for i in range(start, end + 1):
        number_str = str(i)
        length = len(number_str)
        if length % 2 == 1:
            continue
        if number_str[:length // 2] == number_str[length // 2:]:
            subtotal += i
    return subtotal

def add_all_invalid_ids(input_file):   
    with open(input_file, "r") as file:
        line = file.readline().strip()
    ranges = line.split(",")
    sum_of_invalid_ids = 0
    for range in ranges:
        sum_of_invalid_ids += find_subtotal_invalid_ids_in_range(range)
    return sum_of_invalid_ids

def main():
    input = "./day-2/input.txt"
    result = add_all_invalid_ids(input)
    print(f"Sum of all invalid IDs: {result}")

if __name__ == "__main__":
    main()
