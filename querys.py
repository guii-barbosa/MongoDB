from pymongo import MongoClient

# Conectar ao MongoDB
conexao = MongoClient(host=os.getenv("HOST"))
dbConexao = conexao["dbConexao"]
collectionAlunos = dbConexao["alunos"]

# Consulta para encontrar todos os alunos
def buscar_todos_alunos():
    return collectionAlunos.find()

# Consulta para encontrar alunos com idade maior que 18
def buscar_alunos_maiores_de_idade():
    return collectionAlunos.find({"idade": {"$gt": 18}})

# Consulta para encontrar alunos com média menor que 6
def buscar_alunos_media_menor_que_seis():
    return collectionAlunos.find({"media": {"$lt": 6}})

# Consulta para encontrar um aluno pelo nome
def buscar_aluno_por_nome(nome):
    return collectionAlunos.find_one({"nome": nome})

# Consulta para encontrar alunos com média entre 7 e 9
def buscar_alunos_media_entre_sete_e_nove():
    return collectionAlunos.find({"media": {"$gte": 7, "$lte": 9}})

# Consulta para contar o número total de alunos
def contar_total_alunos():
    return collectionAlunos.count_documents({})

# Fechar a conexão com o MongoDB
def fechar_conexao():
    conexao.close()