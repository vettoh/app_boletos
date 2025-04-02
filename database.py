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
                        valor REAL,
                        vencimento DATE,
                        stats TEXT)
''')
    conection.commit() # salva a mudança no banco de dados
    conection.close()
create_table()
print("tabela criada")

def inserir_boleto(empresa, valor, vencimento):
    conection = conectar()
    cursor = conection.cursor()
    cursor.execute ("INSERT INTO boletos (empresa, valor, vencimento, stats) VALUES (?,?, ?, ?)",
                   (empresa, valor, vencimento, 'pendente'))
    conection.commit()
    conection.close ()
inserir_boleto('internet', 99.90, '2027-11-01')
print("boleto inserido")
