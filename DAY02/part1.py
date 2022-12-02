WON = 6
DRAW = 3
LOST = 0

def main():

    lines = open("input.txt").read().splitlines()
    
    totalScore = 0

    for line in lines:
        x = line.split()
        totalScore += ord(x[1]) - 87
        totalScore += rawResult(ord(x[0]) - 64, ord(x[1]) - 87)
    
    print("Total score is ",totalScore)

def rawResult(elf,us):
    if(elf == us):
        return DRAW
    if(elf == 1):
        if(us == 2):
            return WON
        else:
            return LOST
    if(elf == 2):
        if(us == 3):
            return WON
        else:
            return LOST
    if(elf == 3):
        if(us == 1):
            return WON
        else:
            return LOST



if __name__ == '__main__':
    main()