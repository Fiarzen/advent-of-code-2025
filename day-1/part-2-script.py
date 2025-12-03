

def check_0_clicks_after_steps(input, start=50):
    file = open(input, "r")
    lines = file.readlines()
    file.close()
    current_value = start
    zero_count = 0

    def click_count(start, steps):
        count = 0
        if steps > 0:
            for i in range(1, steps + 1):
                if (start + i) % 100 == 0:
                    count += 1
        else:
            for i in range(-1, steps - 1, -1):
                if (start + i) % 100 == 0:
                    count += 1             
        return count
      
    for line in lines:
        if line[0] == "R":
            zero_count += click_count(current_value, int(line[1:]))   
            current_value += int(line[1:])
            current_value %= 100
        else:
            zero_count += click_count(current_value, -int(line[1:]))
            current_value -= int(line[1:])
            current_value %= 100
    return zero_count

def main():
    input = "./day-1/input.txt"
    result = check_0_clicks_after_steps(input)
    print(f"Number of times value is 0: {result}")

if __name__ == "__main__":
    main()
