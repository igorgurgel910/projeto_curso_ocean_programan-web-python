## Curso Programando para web com Python, CSS e HTML

Este repositório foi criado para registrar o conteúdo e os exercícios da Programando para web com Python, CSS e HTML. Este projeto tem como objetivo aprendizado, pois busco transição de carreira para Tecnologia da informação.

Empresa: Ocean Brasil <br>
Nome do curso: Programando para web com Python, CSS e HTML<br>
URL: https://www.oceanbrasil.com/atividades/3061-Programando-para-web-com-Python-CSS-e-HTML<br>
Conteúdo: Faremos uma implementação do python com o HTML e CSS, utilizados para a construção de sites. Com esse curso você vai entender como essa mistura de linguagens funciona e como saber se organizar durante a construção de aplicações, tirando um pouco do medo que temos quando o assunto é combinar diferentes linguagens em uma única aplicação.<br>

- Conhecendo o HTML
- Conhecendo o CSS
- Construindo a primeira página do site
- Páginas estáticas vs páginas dinâmicas
- Entendendo o que é servidor e porque precisamos dele
- Django vs Flask: Entendendo o que são essas tecnologias
- Implementando o Flask
- Exibindo uma página simples
- Integrando a nossa página de HTML e CSS no servidor
- Interagindo com o usuário através do HTML
- Integrando código Python para geração dinâmica do HTML
- Conhecendo alternativas para hospedagem gratuita de sites sem servidor
<br>
Avaliação do curso:<br>

Detalhamento das atividades:

### Aula 01 - 2023/02/13<br>
Nesta aula, conhecemos um pouco sobre GitHub, criando repositório e o professor utilizou gitpod.io para gerenciar a aula.<br>
Foi utilizado o comando pip install flask para instalar essa biblioteca, depois criado um arquivo app.py simples para testar o comando "Hello World".<br>
Foi orientado abrir localhost:5000<br>
Mas não foi possível realizar estas tarefas via VSC desktop.<br>

### Aula 02 - 2023/02/14<br>
Abri o link do repositório no gitpod.io/#<br>
instalar:<br>
  pip install flask<br>
  pip install python-dotenv<br>
  pip freeze> requirements.txt<br>
Criar arquivo '.flaskenv' sem extensão // para executar automático no browser<br>
Usando comandos 'flask run' para rodar<br>
Abrir pasta 'templates'<br>
Criar arquivo 'exibir_entradas.html'<br>
Editar tags HTML <><br>
    html    é principal<br>
    head    cabeça onde ficam os meta dados<br>
    body    onde aparece no corpo da página<br>
    h1      título<br>
    h2      subtítulo<br>
    p       parágrado<br>
    title   escreve o título<br>
    div     agrupar<br>
    a       serve para fazer link (ancora)
<br>
Link da atividade: http://turing.com.br/material/flask/tutorial/templates.html<br>
<br>
Salvar no Git:<br>
  git add .<br>
  git commit -m "commit"<br>
  git push<br>
<br>

### Aula 03 - 2023/02/15<br>
Abri o link do repositório no gitpod.io/#<br>
instalar tudo novamente porque é ambiente virtual:<br>
  pip install flask<br>
  pip install python-dotenv<br>
  pip install -r requirements.txt<br>
Criar rota de login e direcionar a pagina pelo layout<br>
<br>
Instalar o banco de dados de forma local:<br>
  sqlite3 --version <br>
Criou arquivo do banco SQL<br>
Rodou o comando no temrinal - Operador do terminal de bash (shell script):<br>
  sqlite3 blog.bd < esquema.sql<br>
<br>
Inserir manualmente  no banco de dados pelo terminal<br>
sqlite3 blog.bd "INSERT INTO entradas(titulo, texto) VALUES ('Post 1', 'Inserido com sqlite3');"<br>
