
def read_input(file):
    inputs = []
    with open(file) as f:
        inputs = f.readlines()
    f.close()
    return inputs

def  count_increases():
    inputs = read_input("01\\input.txt")
    count = 0
    for idx, value in enumerate(inputs):
        if idx != 0 :
            previous_value = inputs[idx-1]
            if int(previous_value) < int(value) : count += 1
    return count


if __name__ == '__main__':
    increases = count_increases()
    print(increases)