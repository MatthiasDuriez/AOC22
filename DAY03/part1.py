
def main():

    lines = open("input.txt").read().splitlines()

    #test = "vJrwpWtwJgWrhcsFMMfFFhFp"
    #print(len(test)//2)
    #first = test[:len(test)//2]
    #second = test[len(test)//2:]
    #print(first)
    #common_item = list(set(first).intersection(second))[0]
    #print(ord(common_item))

    sumOfPriority = 0

    for line in lines:
        firstCompartment = line[:len(line)//2]
        secondCompartment = line[len(line)//2:]
        common_item = list(set(firstCompartment).intersection(secondCompartment))[0]
        common_item_int = ord(common_item)
        sumOfPriority += common_item_int - 96 if common_item_int > 91 else common_item_int - 38
    
    print("The sum of priority is",sumOfPriority)

if __name__ == '__main__':
    main()