def main():

    lines = open("input.txt").read().splitlines()
    print(lines)
    currentElfCalorie = 0
    listOfElvesCalories = []

    for line in lines:
        if (line == ""):
            listOfElvesCalories.append(currentElfCalorie)
            currentElfCalorie = 0
        else:
            currentElfCalorie += int(line.strip())
    
    print("Max calories is ",max(listOfElvesCalories))

    totalOf3Highest = 0
    for i in range(3):
        totalOf3Highest += max(listOfElvesCalories)
        listOfElvesCalories.remove(max(listOfElvesCalories))
    
    print("Total of 3 highest is ", totalOf3Highest)


if __name__ == '__main__':
    main()