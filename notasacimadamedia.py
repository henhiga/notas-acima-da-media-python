#Renato de Oliveira Melo Filho - 32260377
#Henrique Kenzo Higa - 32256957
final_arquivo = False
string_vazia = ''
nomes=[]
notas=[]
total=0.0
notas_qtd=0

meu_arquivo = open('alunos.txt', 'r')

while not final_arquivo:
    linha = meu_arquivo.readline().rstrip()    
    if linha == string_vazia:
        final_arquivo = True        
    else:
        info_ex1 = linha.split(';')
        nome = info_ex1[0]
        nota = info_ex1[1]
        total+=float(nota)
        notas_qtd+=1
        nomes.append(nome)
        notas_string=float(nota)
        notas.append(notas_string)


media=total/notas_qtd
for i in range(notas_qtd):
    if notas[i]>media:
        print("O ",nomes[i], " Teve uma nota maior que a média(sortudo), ele tirou ",notas[i])
print("Média das notas",media)

meu_arquivo.close()
