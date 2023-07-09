phone=input("phone:")
digits_mapping={
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
c=""
for ch in phone:
    c+= digits_mapping.get(ch,"!")+ " "
    
print(c)    