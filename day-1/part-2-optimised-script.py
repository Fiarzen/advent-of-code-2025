def check_0_clicks_after_steps(input, start=50):
    with open(input, "r") as file:
        lines = file.readlines()

    current_value = start
    zero_count = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        if direction == "R":
            # Count hits at positions where (start + i) % 100 == 0
            # => i = 100 - start, then every +100 more
            if steps >= (100 - current_value):
                zero_count += 1 + (steps - (100 - current_value)) // 100

            current_value = (current_value + steps) % 100

        else:  # "L"
            # Count hits at positions where (start - i) % 100 == 0
            # => i = start, then every +100 more
            if steps >= current_value:
                zero_count += 1 + (steps - current_value) // 100

            current_value = (current_value - steps) % 100

    return zero_count


def main():
    input = "./day-1/input.txt"
    result = check_0_clicks_after_steps(input)
    print(f"Number of times value is 0: {result}")

if __name__ == "__main__":
    main()