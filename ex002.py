nome = input("Como é o seu nome?").strip()
cor1 = '\033[1;35m'
corl = '\033[m'
print("Seja bem-vindo, Senhor {}{}{}!".format(cor1, nome, corl))
personagem = input("Qual é o seu personagem favorito?").strip()
print(f'Este {cor1}{personagem.upper()}{corl} é muito poderoso! :)')
respiraçao = input("Qual é a respiração deste Hashira?").strip()
print(f"Este poder é muito ágil e poderoso, o poder do Pilar da Névoa, a {respiraçao}!")
