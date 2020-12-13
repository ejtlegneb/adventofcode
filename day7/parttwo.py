
# https://likegeeks.com/depth-first-search-in-python/




# Extract a list of lines from file
lines = [x.strip() for x in open('tdata', 'r').readlines()]

bags = {}
q = []
for l in lines:
    # Clean line from unnecessary words.
    l = l.replace('bags', '').replace('bag', '').replace('.','')

    bag, contains = l.split('contain')
    bag = bag.strip()

    if 'no other' in contains: # If bag doesn't contain any bag
        bags[bag] = {}
        continue

    contains = contains.split(',')
    contain_dict = {}
    for c in [c.strip() for c in contains]:
        amount = c[:2]
        color = c[2:]
        contain_dict[color] = int(amount)
    bags[bag] = contain_dict

print(bags)


def recursive_count(bag, bags):
    count = 1  # Count the bag itself

    contained_bags = bags[bag]
    for c in contained_bags:
        multiplier = contained_bags[c]
        count += multiplier * recursive_count(c, bags)
    return count

# Minus one to not count the shiny gold bag itself
result = recursive_count('shiny gold', bags) - 1
print("Result part 2: %d " % result)
