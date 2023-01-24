print("Table of Powers\n")
startInteger = int(input("Start Number: \t"))
stopInteger = int(input("Stop Number:  \t"))
if stopInteger < startInteger:
    print("Error")
else:
    print("Number\tSquared\tCubed")
    for i in range(startInteger, stopInteger+1):
        sq = i**2
        cu = i**3
        print("{}       {}       {}".format(i, sq, cu))
