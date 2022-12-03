WON = 6
DRAW = 3
LOST = 0

def main():

    lines = open("input.txt").read().splitlines()
    
    totalScore = 0

    


    for line in lines:
        x = line.split()
        totalScore += rawResult(ord(x[0]) - 64, ord(x[1]) - 87)
    
    print("Total score is ",totalScore)

def rawResult(elf,result):
    if(result == 2):
        return DRAW + elf
    if(result == 1):
        if(elf == 1):
            return LOST + 3
        if(elf == 2):
            return LOST + 1
        if(elf == 3):
            return LOST + 2
    if(result == 3):
        if(elf == 1):
            return WON + 2
        if(elf == 2):
            return WON + 3
        if(elf == 3):
            return WON + 1

#1:3
#2:1 
#3:2

#1:2
#2:3 
#3:1


if __name__ == '__main__':
    main()