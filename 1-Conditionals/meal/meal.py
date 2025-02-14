time = input("Time? ")
x, y = time.split(":")
x = int(x)
y = int(y)/60
if(7 <= x + y <= 8):
    print("Breakfast Time")
elif(12 <= x + y <= 13):
    print("Lunch Time")
elif(18 <= x + y <= 19):
    print("Dinner Time")
else:
    print("Nothing")