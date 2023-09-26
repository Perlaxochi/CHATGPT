from flask import Flask, request,render_template
import openai

app = Flask(__name__)

conversacion = []

@app.route('/', methods = ["GET","POST"])
def index():
    if request.method =='POST':
        pregunta=request.form.get("pregunta")
        resultado=enviar_pregunta(pregunta)
        conversacion.append(("Yo", pregunta))
        conversacion.append(("ChatGPT", resultado))
    else:
        resultado=""

    return render_template ('index.html', conversacion=conversacion)

def enviar_pregunta(pregunta):
    openai.api_key = "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"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pregunta}
        ],
    )
    respuesta_texto = respuesta["choices"][0]["message"]["content"]
    return respuesta_texto

