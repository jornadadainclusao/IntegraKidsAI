import numpy as np
import os
import pandas as pd

from flask import Flask, render_template, request
from keras.callbacks import EarlyStopping
from keras.layers import Dense
from keras.models import Sequential, load_model
from sklearn.model_selection import train_test_split


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = render_template("index.html")

    if request.method == "POST":
        dificuldade = float(request.form["dificuldade"])
        idade = float(request.form["idade"])
        tentativas = float(request.form["tentativas"])
        erros = float(request.form["erros"])
        input = [dificuldade, idade, tentativas, erros]

        _model = load(MODEL_PATH)
        prediction = predict(_model, input)
        data = render_template("index.html", resultado=prediction)
    return data

MODEL_DATA_DIR = "model"
OUTPUT_MODEL = "model.keras"
DATA_PATH = os.path.join(MODEL_DATA_DIR, "dados.csv")
MODEL_PATH = os.path.join(MODEL_DATA_DIR, OUTPUT_MODEL)

def create(data_path: str, model_path: str):
    # 1) Carregar dados
    df = pd.read_csv(data_path)
    print("Amostras:", len(df))
    print(df.head())

    # 2) Features e target
    X = df[["dificuldade", "idade", "tentativas", "erros"]].values.astype(float)
    y = df["acertos"].values.astype(float)  # regressão: número de acertos

    # 3) Dividir treino/teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4) Criar modelo (simples e compacto)
    model = Sequential([
        Dense(32, activation="relu", input_shape=(X.shape[1],)),
        Dense(16, activation="relu"),
        Dense(1, activation="linear")  # saída contínua (acertos)
    ])
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.summary()

    # 5) Treino (com early stopping)
    es = EarlyStopping(monitor="val_loss", patience=10, restore_best_weights=True)
    history = model.fit(
        X_train, y_train,
        validation_split=0.1,
        epochs=200,
        batch_size=8,
        callbacks=[es],
        verbose=2 # pyright: ignore [reportArgumentType]
    )

    # 6) Avaliar
    loss, mae = model.evaluate(X_test, y_test, verbose=0) # pyright: ignore [reportArgumentType]
    print(f"Teste - MSE: {loss:.4f}, MAE: {mae:.4f}")

    # 7) Salvar o modelo Keras (.h5)
    model.save(model_path)
    print(f"Modelo salvo em {model_path}")

def load(model_path: str):
    # Crie o modelo caso ausente
    if not os.path.exists(MODEL_PATH):
        create(DATA_PATH, MODEL_PATH)

    return load_model(model_path)

def predict(model, input):
    prediction_array = model.predict(np.array([input]))
    prediction = max(0, round(prediction_array[0][0]))
    return prediction

if __name__ == '__main__':
    app.run()
