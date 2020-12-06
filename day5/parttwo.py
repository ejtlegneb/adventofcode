
def twentyfirst_night_of_september():
    with open ("data") as f:
        bpasses = f.read().splitlines()
    
    column = [0, 7]
    row = [0, 127]
    seats = []
    for bpass in bpasses:
        half = 64
        for char in bpass[:7]:
            if char == "B":
                row[0] += half
            if char == "F":
                row[1] -= half
            half /= 2
            # print(char, row, half)
        half = 4
        for char in bpass[7:]:
            if char == "R":
                column[0] += half
            if char == "L":
                column[1] -= half
            half /= 2
    
        seats.append( [int(row[0]), int(column[0])])
        column = [0, 7]
        row = [0, 127]
 
 
    n_list = []
    for seat in seats:
        n_list.append(int(str(seat[0]) + str(seat[1])))
    n_list.sort()
    for i, nr in enumerate(n_list[:-1]):
        if n_list[i+1] - nr > 1 and (n_list[i+1] % 10 != 0 and nr % 10 != 7):
            print(int(sum([nr, n_list[i+1]]) / 2))


if __name__ == "__main__":
    twentyfirst_night_of_september()