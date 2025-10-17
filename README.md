# VidaPLus
gerenciador de unidades de saúde

1 - O arquivo .sql está junto com o projeto com o nome de vidaplus.sql
2 - O arquivo connection/connection.py possui a senha utilizada na criação, caso ocorra algum problema com o banco.
3 - Antes de rodar o arquivo instale o requirements.txt utilizando o pip
4 - Para rodar o app, com ele aberto, utilize no terminal o comando: "flask --app main run"
5 - Isso abrirá a url http://127.0.0.1:5000/ em seu navegador

6 - Para testar a maioria das funcionalidades, entre como admin, com o usuário admin e senha admin
7 - Algumas funcionalidades exigem ser um paciente ou profissional, como registrar uma receita por exemplo
8 - Caso tenha se cadastrado como paciente, o seu login será {primeiro nome}.{ultimo nome}, tudo minusculo com acentos, e a senha o cpf cadastrado
