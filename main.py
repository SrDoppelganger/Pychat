import os

#Menu
print("=================")
print("      Pychat     ")
print("=================")
user = input("Nome de usuário: ")

chat = []

while True:

    #Limpa o Terminal
    os.system('cls')

    print("Digite 'exit' para encerrar o programa")
    if len(chat)> 0:
        for n in chat:
            print(n["user"] + ":" + n["msg"])
    
    print("________________")
    text = input(f"{user}: ")
    if text == "exit":
        break
    else:
        chat.append({"user":user,"msg":text})

    


