


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 10]
    print(memberwise_addition(list1, list2))

def memberwise_addition(list1, list2):
    total = max(list1,list2,key=len)
    if(total == list1):
        for i in range(len(list1)):
            if(i >= len(list2)):
                break
            else:
                total[i] += list2[i]
    if(total == list2):
        for i in range(len(list2)):
            if(i >= len(list1)):
                break
            else:
                total[i] += list1[i]
    return total




if __name__ == "__main__":
    main()
