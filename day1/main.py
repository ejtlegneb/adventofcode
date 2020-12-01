
def ez_solve():

    with open('data') as f:
        numbers = f.read().splitlines()
        numbers = [int(number) for number in numbers]
    for number in numbers:
        find = 2020 - number
        current = number
        for number in numbers:
            if number == find:
                answer = current * find
                print(answer)
                exit()


if __name__ == "__main__":
    ez_solve()