secret_number=8
count=0
limit=3
while count<limit:
    guess=int(input("guess: "))
    
    if guess==secret_number:
        print("u won")
        break
    else:
     count+=1
else:
    print("u lose")    

