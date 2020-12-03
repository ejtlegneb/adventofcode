
def havent_done_my_taxes_im_too_turnt_up():

    with open ('tdata') as f:
        tree_map = f.read().splitlines()

    tree_map = [list(x) for x in tree_map]
    max_v = len(tree_map) -1
    max_h = len(tree_map[0]) -1

    hor_index = 0
    ver_index = 0
    tree_count = 0

    while True:
        if ver_index > max_v:
            break
        if hor_index > max_h:
            hor_index = max_h

        if tree_map[ver_index][hor_index] == '#':
            tree_map[ver_index][hor_index] = 'X'
            tree_count += 1
        else:
            tree_map[ver_index][hor_index] = 'O'
        hor_index += 3
        ver_index += 1


    for line in tree_map:
        for item in line:
            print(item, end='')
        print()
    print(tree_count)



if __name__ == "__main__":
    havent_done_my_taxes_im_too_turnt_up()