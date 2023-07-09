command=input("enter the command ")
if command=="help" :
     C=input("start- to start stop-to stop quit -to quit :")
     while C!=quit:
        
       
        if C=="start":
            print("car started and ready to go")
            break
        elif C=="stop":
            print("car stopped")
            break
     else:
        print("u got exit from game")
else:
    print("i dont understand")                    
   