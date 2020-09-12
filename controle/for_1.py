#

for i in range(10):
  print(i)

for i in range(1, 11):
  print(i)

for i in range(1, 100, 7):
  print(i)

for i in range(20, 0, -3):
  print(i)

nums = [2, 4, 6, 8]

for i in nums:
  print(i)

for i in nums:
  print(i, end=',')

texto = 'Python é muito massa'

for letra in texto:
  print(letra, end=' ')

for n in {1, 2, 3, 4, 4, 4}:
  print(n)

produto = {
  'nome': 'Caneta',
  'preco': 8.80,
  'desc': 0.5
}

for atrib in produto:
  print(atrib, '==>', produto[atrib])

for atrib, valor in produto.items():
  print(atrib, '==>', valor)

for valor in produto.values():
  print(valor, end=' ')

for valor in produto.keys():
  print(valor, end=' ')

