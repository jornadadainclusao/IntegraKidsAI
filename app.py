from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def run():
    data = render_template("index.html")

    if request.method == "POST":
        dificuldade = float(request.form["dificuldade"])
        idade = float(request.form["idade"])
        tentativas = float(request.form["tentativas"])
        erros = float(request.form["erros"])
        input = [dificuldade, idade, tentativas, erros]

        print(model.MODEL_DATA_DIR)
        print(model.DATA_PATH)
        print(model.MODEL_PATH)
        print(model.OUTPUT_MODEL)
        _model = model.load(model.MODEL_PATH)
        prediction = model.predict(_model, input)
        data = render_template("index.html", resultado=prediction)
    return data

if __name__ == '__main__':
    app.run(debug=True)
