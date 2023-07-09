while True:
    command=input(">").lower()
    if command=="start":
        print("car started")
    elif command=="stop":
        print("car stopped ")
    elif command=="help":
        print(""" start- to strt
        stop- to stop
        quit-to quit
        """)   
    elif command=="quit":
        break
else:
    print("sorry i dont understand anything")                 
