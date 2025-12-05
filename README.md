# IntegraKidsAI

Este projeto tem o objetivo de construir e treinar um modelo de rede neural
para prever a quantidade de acertos de um jogador em um jogo genérico da
plataforma, baseando-se em um conjunto de métricas de desempenho fornecido pelo
usuário através de uma página web.

As métricas de desempenho consistem em:
- dificuldade do jogo;
- idade do usuário;
- quantidade de tentativas;
- quantidade de erros.

A página web, seguindo o [modelo de Flask da Azure](https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart), encontra-se hospedada no seguinte link:
https://integrakids-ai.azurewebsites.net/

## Características do Projeto:
- **Treinamento do Modelo**: as redes neurais foram treinadas usando
  [Keras](https://keras.io/) e
  [Scikit-learn](https://scikit-learn.org/stable/index.html).
- **Interatividade**: o usuário insere métricas anteriores do jogador para
  prever seu desempenho.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Pandas**: Para manipulação e análise de dados.
- **NumPy**: Para operações matemáticas e manipulação de arrays.
- **Scikit-learn**: Para modelos de machine learning.
- **Flask**: Para criação da interface web interativa.
