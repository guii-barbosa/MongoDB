from pymongo import MongoClient

#conexão com o mongo
conexao = MongoClient(host="mongodb://localhost:27017")

#criar um banco de dados
dbConexao = conexao["dbConexao"]

#criar uma collection
collectionAlunos = dbConexao["alunos"]

#(C) - criação de documentos
aluno1 = {
    "nome":"Marcelo",
    "sobrenome":"Grilo",
    "idade":16,
    "media":7.4
}

# collectionAlunos.insert_one(aluno1)

#(R) - leitura de documentos
documentos = collectionAlunos.find() 
# traz um cursor, estrutura de dados que precisa ser "varrida"
for doc in documentos:
    for campo in doc:
        print(campo,":",doc[campo])
        
#(U) - atualização de documentos
filtro = {"nome":"Marcelo"}
resultado_update = collectionAlunos.update_one(filtro,{"$set":{"media":9.1}})
print("Documentos atualizados:", resultado_update.modified_count)

#(D) - deletar um documento
resultado_delete = collectionAlunos.delete_one({"nome":"Marcelo"})
print("Documentos deletados:", resultado_delete.deleted_count)

#exluir database
conexao.drop_database(dbConexao)
