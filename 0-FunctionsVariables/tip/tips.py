Cost = input("How much was the meal? ")
Percent = input("What percent would you like to tip? ")
Cost = float(Cost)
Percent = Percent.replace("%",(""))
Percent = float(Percent)
Percent = Percent*0.01
Tip = Cost * Percent
print("Leave $",Tip,sep="")