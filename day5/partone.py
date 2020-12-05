
def twentyfirst_night_of_september():
    with open ("data") as f:
        bpasses = f.read().splitlines()
    
    column = [0, 7]
    row = [0, 127]
    highest = 0
    for bpass in bpasses:
        half = 64
        for char in bpass[:7]:
            if char == "B":
                row[0] += half
            if char == "F":
                row[1] -= half
            half /= 2
        half = 4
        for char in bpass[7:]:
            if char == "R":
                column[0] += half
            if char == "L":
                column[1] -= half
            half /= 2
    
        if row[0] * 8 + column[0] > highest:
            highest = row[0] * 8 + column[0]
        column = [0, 7]
        row = [0, 127]
    print(int(highest))

if __name__ == "__main__":
    twentyfirst_night_of_september()