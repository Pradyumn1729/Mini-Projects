weight=float(input("what is ur  weight?  "))
what=(input("put p(pounds) or k(kilograms): "))
if what.upper()=="K":
    pound=float(weight)/ 0.45
    print(pound)
elif what.upper()=="P":
    kilogram =float(weight) *0.45
    print(kilogram)  
else:
    print("invald choice entered")    
