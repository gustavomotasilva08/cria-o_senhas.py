import string

print("=== CRIAÇÃO DE SENHA ===")

senha = input("Crie sua senha: ")

primeira_maiuscula = senha[0].isupper()
tem_pontuacao = any(c in string.punctuation for c in senha)
tem_8_caracteres = len(senha) >= 8

print("\n=== VERIFICAÇÃO ===")

if primeira_maiuscula and tem_pontuacao and tem_8_caracteres:
    print(" Senha criada com sucesso!")
    print(" Senha forte!")
else:
    print(" A senha não atende aos requisitos:")

    if not primeira_maiuscula:
        print("- O primeiro caractere deve ser uma letra maiúscula.")

    if not tem_pontuacao:
        print("- A senha deve conter uma pontuação (!, @, #, $, %, etc.).")

    if not tem_8_caracteres:
        print("- A senha deve ter pelo menos 8 caracteres.")