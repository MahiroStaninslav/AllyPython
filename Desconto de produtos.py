nome = str(input('Bem-Vindo(a), Como é o seu nome? '))
cargo = str(input('Qual cargo o Senhor(a) ocupa? '))
preco = float(input('Muito bem {} {}, Diga o preço do produto desejado e eu aplicarei o desconto:'.format(cargo, nome)))
desconto = 0.05 * preco
total = preco - desconto
print('O valor do produto escolhido com o desconto de 5% fica {:.2f}R$.'.format(total))
