import re

def id_say_love_was_a_magical_flame():

    with open("data") as f:
        passports = [re.findall(r"[\w#]+", x) for x in f.read().split("\n\n")]

    valid = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    valid_c = 0

    for passport in passports:
        count = 0
        for field in range(0, len(passport), 2):
            if passport[field] in valid:
                count += 1
        if count >= 7:
            valid_c += 1
    print(valid_c)
  




if __name__ == "__main__":
    id_say_love_was_a_magical_flame()