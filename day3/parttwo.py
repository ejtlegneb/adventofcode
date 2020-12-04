import fileinput

def im_luke_skywalkin(hor: int, ver: int):

    count = 0
    hor_i = 0
    ver_i = 0

    with open ('data') as f:
        tree_map = f.read().splitlines()
    tree_map = [list(x) for x in tree_map]

    while ver_i + 1 < len(tree_map):
        hor_i += hor
        ver_i += ver
        if tree_map[ver_i][hor_i % len(tree_map[ver_i])]=='#':
            count += 1

    return count

if __name__ == "__main__":
    s1 = im_luke_skywalkin(1, 1)
    s5 = im_luke_skywalkin(3, 1)
    s2 = im_luke_skywalkin(5, 1)
    s3 = im_luke_skywalkin(7, 1)
    s4 = im_luke_skywalkin(1, 2)
    print(s1 * s2 * s3 * s4 * s5)
