for i in range(30000000,100000000,1):
    with open("passwdy.txt","a") as file:
        file.write(f"{i}\n")
