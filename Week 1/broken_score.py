"""
CP1404/CP5632 - Practical Solution
Broken program to determine score status
Update: FIXED
"""

# todo: Fix this!
# Update: FIXED
def fixed_solution(score):
    if(0 < score < 50):
        print("Bad")
    elif(50 <= score < 90):
        print("Passable")
    elif(90 <= score <= 100):
        print("Excellent")
    else:
        print("Invalid Score")

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
    score = float(input("Enter score: "))
    fixed_solution(score)

if __name__ == "__main__":
    main()