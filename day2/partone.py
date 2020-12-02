
def still_ez():
    with open('data') as f:
        passwords = f.read().splitlines()

    valid_count = 0
    for line in passwords:
        count = 0
        policy, password = line.replace(" ", "").split(':')
        policy_freq = [int(x) for x in policy[:-1].split('-')]
        policy_let = policy[-1]
        for letter in password:
            if letter == policy_let:
                count += 1
        if count >= policy_freq[0] and count <= policy_freq[1]:
            valid_count += 1
    print(valid_count)

if __name__ == "__main__":
    still_ez()