
from flask import Flask, render_template, request, redirect, url_for, session, flash

from sistema_especialista.fatos import (
    criar_base_fatos,
    registrar_resposta,
    obter_descricao
)

from sistema_especialista.questionario import (
    CATEGORIAS_QUESTIONARIO,
    obter_proxima_pergunta
)

from sistema_especialista.motor_inferencia import executar_inferencia


app = Flask(__name__)

# Chave provisória para utilizar sessões durante o desenvolvimento.
# Posteriormente, podemos configurar uma chave segura por variável de ambiente.
app.secret_key = "tech-expert-chave-desenvolvimento"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/iniciar")
def iniciar():
    return render_template(
        "categorias.html",
        categorias=CATEGORIAS_QUESTIONARIO
    )


@app.route("/diagnostico/<categoria>", methods=["POST"])
def iniciar_diagnostico(categoria):

    if categoria not in CATEGORIAS_QUESTIONARIO:
        flash("Categoria inválida.")
        return redirect(url_for("iniciar"))

    # Inicia uma nova sessão de diagnóstico.
    session["categoria"] = categoria
    session["respostas"] = {}

    return redirect(url_for("questionario"))


@app.route("/questionario")
def questionario():

    categoria = session.get("categoria")

    if not categoria:
        return redirect(url_for("iniciar"))

    respostas = session.get("respostas", {})

    pergunta = obter_proxima_pergunta(categoria, respostas)

    # Se não houver mais perguntas, processa o diagnóstico.
    if pergunta is None:

        base_fatos = criar_base_fatos()

        for fato, resposta in respostas.items():
            registrar_resposta(base_fatos, fato, resposta)

        resultado = executar_inferencia(base_fatos)

        diagnosticos = [
            {
                "identificador": fato,
                "descricao": obter_descricao(fato)
            }
            for fato in resultado["diagnosticos"]
        ]

        return render_template(
            "resultado.html",
            diagnosticos=diagnosticos,
            historico=resultado["historico"],
            categoria=CATEGORIAS_QUESTIONARIO[categoria]
        )

    total_perguntas = len(respostas)

    return render_template(
        "questionario.html",
        pergunta=pergunta,
        categoria=CATEGORIAS_QUESTIONARIO[categoria],
        total_perguntas=total_perguntas
    )


@app.route("/responder", methods=["POST"])
def responder():

    if "categoria" not in session:
        return redirect(url_for("iniciar"))

    fato = request.form.get("fato")
    resposta = request.form.get("resposta")

    if resposta not in ("sim", "nao"):
        flash("Selecione uma resposta válida.")
        return redirect(url_for("questionario"))

    respostas = session.get("respostas", {})

    respostas[fato] = resposta == "sim"

    session["respostas"] = respostas

    return redirect(url_for("questionario"))


@app.route("/novo-diagnostico")
def novo_diagnostico():

    session.pop("categoria", None)
    session.pop("respostas", None)

    return redirect(url_for("iniciar"))


if __name__ == "__main__":
    app.run(debug=True)
