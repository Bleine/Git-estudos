print("Hello, world")

print("Git Quest - Fase 1 - O repositório")

#começa com uma pergunta 
print("Qual comando é utilizado para iniciar um repositório git?")

#Comparar a resposta
while True:
    resposta = input()
    print(f"A resposta é: {resposta}")
    if resposta == "git init":
        print("Certa resposta!!!!!!!!")
        break
    else:
        print("Tente novamente")
        

print("Qual comando é utilizado para checar o status do reposório")

#comparar a resposta
while True:
    resposta = input()
    print("A resposta é:", end = "" )
    