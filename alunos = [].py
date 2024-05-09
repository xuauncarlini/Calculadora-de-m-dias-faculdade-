alunos = []
aprovados = []
reprovados = []
for total in range(0,100):
  print(f'\naluno {total+1}:')
  
  #estabelecendo notas
  n1 = float(input("nota aop1 (de zero a um ponto): "))
  if not 1>=n1>=0:
    print("o número deve ser entre 0 e 1")
    break
  n2 = float(input("nota aop2 (de zero a dois pontos): "))
  if not 2>=n2>=0:
    print("o número deve ser entre 0 e 2")
    break
  n3 = float(input("nota aop3 (de zero a um ponto): "))
  if not 1>=n3>=0:
    print("o número deve ser entre 0 e 1")
    break
  n4 = float(input("prova regular (de zero a seis pontos): "))
  if not 6>=n4>=0:
    print("o número deve ser entre 0 e 6")
    break

  #somando e tirando média para ver aprovados e reprovados 
  soma = (n1 + n2 + n3 + n4)
  print("pontos das aops e prova regular:",soma)
  if soma >= 7:
    alunos.append(1)
    aprovados.append(1)
    print("aprovado")
  
    
  else:
    print("está de recuperação")
    n5 = float(input("prova recuperação (de zero a dez pontos): "))
    if not 10>=n5>=0:
      print("o número deve ser entre 0 e 10")
      break
    recu = ((soma + n5)/2)
    if recu >= 5:
      print("aprovado")
      aprovados.append(1)
      alunos.append(1)
    else:
      print("reprovado")
      reprovados.append(0)
      alunos.append(0)
    

  #tirando porcentagem e mostarndo resultados
  percentualapro = ((len(aprovados)/len(alunos))*100)
  print("porcentagem aprovados: ",percentualapro,"%")
  percentualrepro = ((len(reprovados)/len(alunos))*100)
  print("porcentagem reprovados: ",percentualrepro,"%")
  print("total de alunos: ", len(alunos))