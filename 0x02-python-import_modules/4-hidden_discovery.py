#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    i = 0
    file = dir(hidden_4)
    file.sort()
    for name in file:
        if name[0] != '_' and name[1] != '_':
            print(file[i])
        i += 1
