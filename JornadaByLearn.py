# Registra aluno na chamada

chamada = []
flag = True

while(flag):
  nome_aluno = input('Digite o nome do Aluno que deseja registrar na chamada ou 0 para sair')
  chamada.append(nome_aluno.lower())
  chamada = sorted(chamada)
  print(chamada)
  if not(nome_aluno):
    flag = False
