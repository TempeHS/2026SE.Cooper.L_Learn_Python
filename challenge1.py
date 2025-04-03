l_1 = [1,3,2,4,5]
l_2 = ["a","b","c","d","e"]
l_1.sort()
'''
def print_table():
    global l_1
    global l_2
    print("| Col 1 | Col 2 |")
    print("| --- | --- |")
    for(i) in l_1:
        print("|", end="")
        print((i), end="|")
        print(l_2[i - 1] + "|")


print_table()
num = int(input("1-5 "))
print(l_2[num-1])
l_1.append(6)
l_2.append("f")
l_2.sort()
l_1.sort()
print_table()


'''
s_1 = ','.join(str(x) for x in l_1)
s_2 = ",".join(str(x) for x in l_2)

file = open("challenge1.txt", "w")
file.write(f'{s_1}\n')
file.write(f'{s_2}\n')
file.close()

