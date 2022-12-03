
def main():

    lines = open("input.txt").read().splitlines()

    sumOfPriority = 0

    for i in range(0, len(lines),3):
        firstElf = lines[i]
        secondElf = lines[i+1]
        thirdElf = lines[i+2]

        common_item = list(set(firstElf).intersection(secondElf,thirdElf))[0]
        common_item_int = ord(common_item)
        sumOfPriority += common_item_int - 96 if common_item_int > 91 else common_item_int - 38

        
        print("Common letter is ",common_item,common_item_int)
        print("The string were",firstElf,secondElf,thirdElf)
        print("the priority is",common_item_int - 96 if common_item_int > 91 else common_item_int - 38)

    print("The sum of priority is",sumOfPriority)

if __name__ == '__main__':
    main()