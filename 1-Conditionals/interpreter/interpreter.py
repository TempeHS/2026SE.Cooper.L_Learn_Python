Ans = input("Equation? ")
x, y, z = Ans.split(" ")

if y.find("+") != -1:
    print(round(float(x)+float(z), 1))
if y.find("-") != -1:
    print(round(float(x)-float(z), 1))
if y.find("*") != -1:
    print(round(float(x)*float(z), 1))
if y.find("/") != -1:
    print(round(float(x)/float(z), 1))