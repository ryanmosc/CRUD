import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='q1w2e3',
    database='bdyoutube'
)
cursor = conexao.cursor()

# CRUD




cursor.close()
conexao.close()

#Comando de adicionar

nome = str(input("Qual o nome do produto que deseja adicionar?"))
valor = int(input("Qual o valor do produto?"))
comando = f'INSERT INTO vendas (nome_produto,valor) VALUES ("{nome}",{valor})' #Faz o comando SQL E todo comando SQL tem que ser entre aspas simples ''
cursor.execute(comando) #Executa o 'comando'
conexao.commit() #Edita o banco de dados

#Comando de ver a lista

comando = f'SELECT * FROM vendas;' #Faz o comando SQL E todo comando SQL tem que ser entre aspas simples ''
cursor.execute(comando) #Executa o 'comando'
resultado = cursor.fetchall() #Ler o banco de dados
print(resultado)

#Comando de update

#Mostra o banco de dados para o cliente saber o que esta fazendo

comando = f'SELECT * FROM vendas;' 
cursor.execute(comando) 
resultado = cursor.fetchall() 
print(resultado)

# #Comando de editar

valor = int(input("Qual o valor do produto a ser adicionado?"))
nome = str(input("Qual o nome do pdrotudo?"))
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome}"' 
cursor.execute(comando)
conexao.commit() 

# #Mostra novamente o banco de dados com a alteraçaõ

comando = f'SELECT * FROM vendas;' 
cursor.execute(comando) 
resultado = cursor.fetchall()
print(resultado)

#Comando de Deletar

idRemover = int(input('Qual o id do produto que deseja remover?'))
comando = f'DELETE FROM vendas WHERE idVendas = {idRemover}'
cursor.execute(comando)
conexao.commit()

