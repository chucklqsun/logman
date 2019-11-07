def read_file(path):
    ret = []
    f = open(path, "r")
    f1 = f.readlines()
    for x in f1:
        ret.append(x)
    return ret
