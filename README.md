# Conexão com o MongoDB

O MongoDB é um sistema de gerenciamento de banco de dados (SGBD) não relacional, também conhecido como NoSQL. Ele difere dos bancos de dados relacionais tradicionais, como o MySQL ou PostgreSQL, em sua estrutura de armazenamento e modelo de dados.

Para realizar a conexão de uma banco não relacional com o Python precisamos instalar a biblioteca `pymongo`, a biblioteca oficial do MongoDB para Python que permite interagir de forma fácil e eficiente.

No código realizamos a criação do banco `dbConexao` e a da collection `alunos`. Após isso, o proceso de CRUD é realizado com inserção, leitura, atualização e remoção dos dados. Por fim, o database é excluído por inteiro.

Para realizar a instalação deste projeto, basta clonar o repositório com o código `git clone https://github.com/guii-barbosa/MongoDB.git` e mudar o host e porta se necessário. Depois disso, basta rodar o código e ele irá realizar todo o processo de CRUD.