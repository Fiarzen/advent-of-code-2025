def check_if_0_after_steps(input, start=50):
    file = open(input, "r")
    lines = file.readlines()
    file.close()
    current_value = start
    zero_count = 0
    for line in lines:
        if line.startswith("R"):
            current_value += int(line[1:])
            current_value %= 100
        elif line.startswith("L"):
            current_value -= int(line[1:])
            current_value %= 100
        if current_value == 0:
            zero_count += 1
    return zero_count

def main():
    input = "./day-1/input.txt"
    result = check_if_0_after_steps(input)
    print(f"Number of times value is 0: {result}")

if __name__ == "__main__":
    main()
