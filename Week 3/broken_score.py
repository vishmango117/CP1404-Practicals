"""
CP1404/CP5632 - Practical Solution
Broken program to determine score status
Update: FIXED
"""

# todo: Fix this!
# Update: FIXED
#Update: From Week 1's source code instead of printing the output i have returned the statement
def fixed_solution(score):
    if(0 < score < 50):
        return "Bad"
    elif(50 <= score < 90):
        return "Passable"
    elif(90 <= score <= 100):
        return "Excellent"
    else:
        return "Invalid Score"

"""def invalid_solution(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        if score > 50:
            print("Passable")
        if score > 90:
        print("Excellent")
    if score < 50:
        print("Bad")"""

def main():
    flag = True
    while flag:
        try:
            score = float(input("Enter score: "))
        except ValueError:
            print("Invalid Option Try Again..!!")
    print(fixed_solution(score))


if __name__ == "__main__":
    main()
