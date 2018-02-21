porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cao1 = [1, 1, 1]
cao2 = [0, 1, 1]
cao3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cao1, cao2, cao3]

marcacoes = [1, 1, 1, -1, -1, -1]

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

teste = [misterioso1, misterioso2, misterioso3]

marcacao_teste = [-1, 1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(dados, marcacoes)
resultado = modelo.predict(teste)

erros = resultado - marcacao_teste

#[for erro in erros if erro != 0]

print(resultado)

diferencas = resultado - marcacao_teste

print(diferencas)

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste)
total_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(total_de_acertos)
print(total_de_elementos)
print(total_de_acerto)

