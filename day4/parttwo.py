import re
import collections

def convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def id_say_love_was_a_magical_flame():

    with open("data") as f:
        passports = [re.findall(r"[\w#]+", x) for x in f.read().split("\n\n")]

    valid_c = 0
    for passport in passports:
        c_pp = convert(passport)
        if "cid" in c_pp:
            del c_pp["cid"]
        if "byr" in c_pp and int(c_pp["byr"]) >= 1920 and int(c_pp["byr"]) <= 2002 and \
            "iyr" in c_pp and int(c_pp["iyr"]) >= 2010 and int(c_pp["iyr"]) <= 2020 and \
             "eyr" in c_pp and int(c_pp["eyr"]) >= 2020 and int(c_pp["eyr"]) <= 2030 and \
              "ecl" in c_pp and (c_pp["ecl"] == "amb" or c_pp["ecl"] == "blu" or c_pp["ecl"] == "brn" or \
               c_pp["ecl"] == "gry" or c_pp["ecl"] == "grn" or c_pp["ecl"] == "hzl" or c_pp["ecl"] == "oth") and \
                "hgt" in c_pp and ((c_pp["hgt"][-2:] == "cm" and int(c_pp["hgt"][:-2]) >= 150 and int(c_pp["hgt"][:-2]) <= 193)  or \
                 (c_pp["hgt"][-2:] == "in" and int(c_pp["hgt"][:-2]) >= 59 and int(c_pp["hgt"][:-2]) <= 76)):
            if "hcl" in c_pp and c_pp["hcl"][0] == '#' and len(c_pp["hcl"]) == 7:
                for char in c_pp["hcl"][1:]:
                    if not char.isdigit():
                        letters = ["a", "b", "c", "d", "e", "f"]
                        if char not in letters:
                            continue
                if "pid" in c_pp and len(c_pp["pid"]) == 9:
                    for char in c_pp["pid"]:
                        if not char.isdigit():
                            continue
                    print(collections.OrderedDict(sorted(c_pp.items())))
                    valid_c += 1
    print(valid_c)


if __name__ == "__main__":
    id_say_love_was_a_magical_flame()
