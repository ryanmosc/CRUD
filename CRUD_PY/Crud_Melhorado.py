import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='q1w2e3',
    database='bdyoutube'
)
cursor = conexao.cursor()

def criar(cursor,conexao):
    nome = str(input("Qual o nome do produto que deseja adicionar?"))
    valor = int(input("Qual o valor do produto?"))
    comando = f'INSERT INTO vendas (nome_produto,valor) VALUES ("{nome}",{valor})' #Faz o comando SQL E todo comando SQL tem que ser entre aspas simples ''
    cursor.execute(comando) #Executa o 'comando'
    conexao.commit() #Edita o banco de dados
    print("Produto adicionado com sucesso!")

def ler_tabela(cursor):
    comando = f'SELECT * FROM vendas;' #Faz o comando SQL E todo comando SQL tem que ser entre aspas simples ''
    cursor.execute(comando) #Executa o 'comando'
    resultado = cursor.fetchall() #Ler o banco de dados
    print(resultado)
    
def update(cursor, conexao):
    comando = f'SELECT * FROM vendas;' 
    cursor.execute(comando) 
    resultado = cursor.fetchall() 
    print(resultado)
    print("Produto editado com sucesso!")
# #Comando de editar
    nome = str(input("Qual o nome do pdrotudo?"))
    valor = int(input("Qual o valor do produto a ser adicionado?"))
    comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome}"' 
    cursor.execute(comando)
    conexao.commit() 
# #Mostra novamente o banco de dados com a alteraçaõ
    comando = f'SELECT * FROM vendas;' 
    cursor.execute(comando) 
    resultado = cursor.fetchall()
    print(resultado)

def deletar(cursor, conexao):
    idRemover = int(input('Qual o id do produto que deseja remover?'))
    comando = f'DELETE FROM vendas WHERE idVendas = {idRemover}'
    cursor.execute(comando)
    conexao.commit()
    print("Produto deletado com sucesso!")

def main():
   
    
    while True:
        print("BEM VINDO AO MEU PRIMEIRO PROJETO DE 'CRUD'")
        print("NESSE PROJETO UTILIZEI PYTHON E MYSQL")
        inicio = input("Aperte qualquer tecla para continuar")
        print("Escolha uma das opcoes seguintes [1]Adicionar [2]Ver o banco [3]Editar [4]Remover [5] Sair")
        opcao = (input(""))
        if opcao == 1:
            criar(cursor,conexao)
            
        elif opcao == 2:
            ler_tabela(cursor)
            
        elif opcao == 3:
            update(cursor, conexao)
            
        elif opcao == 4:
            deletar(cursor, conexao)
        
        elif opcao == 5:
            break
        
        else:
            print("Escolha uma opção valida")
    
    cursor.close()
    conexao.close()
    
if __name__ == '__main__':
    main()
            
        