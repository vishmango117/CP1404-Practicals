
def main():
    numbers = []
    for i in range(5):
        print("Enter Number {}:".format(i+1))
        numbers.append(int(input()))
        print("Number: ",numbers[i])
    print("The first number is",numbers[0])
    print("The last number is",numbers[len(numbers) - 1])
    print("The smallest number is",min(numbers))
    print("The largest number is ", max(numbers))
    print("The Average of the numbers is:",sum(numbers)/len(numbers))


if __name__ == "__main__":
    main()