import sqlite3
# TEMOS QUE CRIAR UMA FUNÇÃO DE CONEXÃO COM O BANCO DE DADOS
def conectar():
    conection = sqlite3.connect(r"C:\Users\User\Desktop\git\app_boletos\boletos.db")
    return conection # retornamos conection aqui para que outras funções possam usar ela depois
# aqui criaremos uma tabela para armazenar os boletos
def create_table():
    conection = conectar() # aqui chamamos o banco de dados para dentro da função
    cursor = conection.cursor() # aqui criamos um cursor que é um comando para que possamos interagir com o banco de dados criando tabelas ou inserir dados
    # aqui passamos os objetos da tabela como nome das colunas, e usamos "id integer primary KEY AUTOINCREMENT" para criar uma coluna com o número dos boletos e usamos PRIMARY KEY AUTO INCREMENT para ir somando o número dos boletos automaticamente
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS boletos (
                        id integer primary KEY AUTOINCREMENT, 
                        empresa TEXT,
                        datadacompra DATE,
                        valor REAL,
                        parcelas REAL,
                        vencimento DATE,
                        stats TEXT)
''')
    conection.commit() # salva a mudança no banco de dados
    conection.close()
create_table()
print("tabela criada")

def inserir_boleto(empresa, datadacompra, valor, parcelas, vencimento):
    conection = conectar()
    cursor = conection.cursor()
    cursor.execute ("INSERT INTO boletos (empresa, datadacompra, valor, parcelas, vencimento, stats) VALUES (?,?, ?, ?, ?,?)",
                   (empresa, datadacompra, valor, parcelas, vencimento, 'pendente'))
    conection.commit()
    conection.close ()

print("boleto inserido")

def ver_boletos():
    conn = sqlite3.connect('boletos.db') # faz a conexão com o banco de dados
    cursor = conn.cursor() # cursor é o objeto que executa comando no SQL

    cursor.execute("SELECT* FROM boletos") # busca todos os dados na tabela
    resultado = cursor.fetchall() # pega todos os dados da tabela em forma de tuplas
    
    conn.close() # fecha a conexão com o banco
    return resultado
