def havent_done_my_taxes_im_too_turnt_up():

    ver_i = 0
    hor_i = 0
    count = 0

    with open ('tdata') as f:
        tree_map = f.read().splitlines()

    tree_map = [list(x) for x in tree_map]

    while ver_i + 1 < len(tree_map):
        hor_i += 3
        ver_i += 1

        if tree_map[ver_i][hor_i % len(tree_map[ver_i])]=='#':
            tree_map[ver_i][hor_i % len(tree_map[ver_i])] = 'X'
            count += 1
        else:
            tree_map[ver_i][hor_i % len(tree_map[ver_i])] = 'O'

    for line in tree_map:
        for item in line:
            print(item, end='')
        print()
    print(count)

if __name__ == "__main__":
    havent_done_my_taxes_im_too_turnt_up()