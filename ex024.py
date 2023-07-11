cidade = str(input('Como é o nome de sua cidade? ')).strip()
cidade = (cidade.title().split())
print(cidade)
Santo = "Santo" in cidade[0]
print('O nome desta cidade se inicia com o nome "Santo"? {}'.format(Santo))
