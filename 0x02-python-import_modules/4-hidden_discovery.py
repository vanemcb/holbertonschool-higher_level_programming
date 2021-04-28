#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    file = dir(hidden_4)
    file.sort()
    for i in range(8, 11):
        print(file[i])
