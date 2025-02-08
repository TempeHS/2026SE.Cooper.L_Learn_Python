text = input("Greeting? ")
text = text.lower()
text = text.strip()
if text.find(" ") != -1:
    first, last = text.split(" ")
    text = first

if (text == "hello"):
    print("$0")
elif (text[0] == "h"):
    print("$20")
else:
    print("$100")