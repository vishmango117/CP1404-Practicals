"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    subjects = scores_data[0].strip().split(",")

    score_values = []
    score_values2 = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
     
    
    score_values2 = [[score_values[j][i] for j in range(len(score_values))] for i in range(len(score_values[0]))]
    for cols in range(len(subjects)):
        score_values2[cols].insert(0,subjects[cols])
    print("\n")
    
    for row in score_values2:
        print(row[0],end =' ')
        for cols in row[1:]:
            print(cols, end=' ')
        print("Max:",max(row[1:]),end =' ')
        print()
    

    
    
    print()

if __name__ == "__main__":
    main()