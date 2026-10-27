import sys


if __name__ == "__main__":
    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])

    interest = (p * r * t) / 100
    print("Simple interest: ", interest)