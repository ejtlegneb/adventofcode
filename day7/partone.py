def lets_get_medicated():

    with open ('data') as f:
        bags_rows = f.read().splitlines()

    hold_gold = []
    for row in bags_rows:
        row = row.split("contain")
        for bag in row[1:]:
            if bag.find("shiny gold") != -1:
                hold_gold.append(row[0])
    hold_gold = [x.replace("bags ", '').replace("bag", "").strip() for x in hold_gold]
    i = 0
    while i < len(bags_rows):
        row = bags_rows[i].split("contain")
        for bag in row[1:]:
            bag = bag.split(",")
            for b in bag:
                if b.replace("bags", '').replace("bag", "").replace(".", "").strip()[2:] in hold_gold:
                    if row[0].replace("bags", '').replace("bag", "").replace(".", "").strip() not in hold_gold:
                        hold_gold.append((row[0].replace("bags", '').replace("bag", "").replace(".", "").strip()))
                        i = -1
        i += 1

    print(len(hold_gold))


if __name__ == "__main__":
    lets_get_medicated()