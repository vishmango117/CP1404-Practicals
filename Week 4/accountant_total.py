#CP1404 Programming II W4 Practical


def get_income_and_total(months):
    income = []
    total = []
    curr_total = 0
    for i in range(months):
        print("Enter income for month",i+1,": ")
        curr_income = float(input())
        income.append(curr_income)
        curr_total += curr_income
        total.append(curr_total)

    return (income,total)



def main():
    months = int(input("How many months? "))
    income,total = get_income_and_total(months)
    print("Income Report")
    print("----------------")
    for i in range(months):
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(i+1, income[i], total[i]))

if __name__ == "__main__":
    main()