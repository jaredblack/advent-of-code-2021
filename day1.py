def solve_a():
    in_file = open('in1.txt', 'r')
    readings = [int(num) for num in in_file.read().split()]
    in_file.close()
    prev_reading = readings[0]
    increasing = 0
    for reading in readings:
        if reading > prev_reading:
            increasing += 1
        prev_reading = reading
    return increasing

def solve_b():
    in_file = open('in1.txt', 'r')
    readings = [int(num) for num in in_file.read().split()]
    in_file.close()
    increasing = 0
    for i in range(2, len(readings) - 1):
        sumA = sum(readings[i-2:i+1])
        sumB = sum(readings[i-1:i+2])
        if sumB > sumA:
            increasing += 1
    return increasing

if __name__ == "__main__":
    print(solve_b())