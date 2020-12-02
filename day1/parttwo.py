def ez_solve():

    with open('data') as f:
        numbers = f.read().splitlines()
        numbers = [int(number) for number in numbers]


    for number in numbers:
        first_number = number

        for number in numbers:
            second_number = number

            for number in numbers:
                thirth_number = number
                if thirth_number + second_number + first_number == 2020:
                    print(thirth_number * second_number * first_number)
                    exit()

if __name__ == "__main__":
    ez_solve()