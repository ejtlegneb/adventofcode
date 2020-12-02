
def still_ez():
    with open('data') as f:
        passwords = f.read().splitlines()

    valid_count = 0
    for line in passwords:
        count = 0
        policy, password = line.replace(" ", "").split(':')
        indices = [int(x)-1 for x in policy[:-1].split('-')]
        policy_let = policy[-1]
        password_list = list(password)
        if (password_list[indices[0]] == policy_let and password_list[indices[1]] != policy_let) or \
            (password_list[indices[1]] == policy_let and password_list[indices[0]] != policy_let):
            valid_count += 1

    print(valid_count)

if __name__ == "__main__":
    still_ez()