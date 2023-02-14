from flask import Flask, render_template

app = Flask("__name__")

# POSTS MOCK - simulação da página antes de criar o banco de dados, algo de mentira que utiliza para fazer testes
posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu primeiro Post"
    },
    {
        "titulo": "Post 2",
        "texto": "Meu primeiro Post"
    },
    {
        "titulo": "Post 3",
        "texto": "New Post"
    }

]

@app.route("/")
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)

@app.route("/pudim")
def pudim():
    return "<h1>eu gosto de pudim</h1>"
