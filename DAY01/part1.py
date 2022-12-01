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



if __name__ == '__main__':
    main()