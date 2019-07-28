#CP1404 Programming II Playing with format in for loops


for i in range(0,100000,100):
    print("{:>6}".format(i),end='')
    print("\t {:<3}".format(i))