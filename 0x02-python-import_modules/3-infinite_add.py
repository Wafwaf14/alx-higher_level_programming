#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lasomme = 0
    for k in range(len(sys.argv) - 1):
        lasomme += int(sys.argv[k + 1])
    print("{}".format(lasomme))
