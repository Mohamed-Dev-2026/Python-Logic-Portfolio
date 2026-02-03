attendees = input("entrer the names of attendees by commas ").split(",")
print()
for person in attendees :
    print(f"{person} \n")
    response =input("is the person attending? (yes\on)")
    if response =="yes":
        print("attendance confirmed")
    else:
        print("attendance not confirmed")
    print("_ _ _ _ _ _")
