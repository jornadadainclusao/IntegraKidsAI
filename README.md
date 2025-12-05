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
- **Treinamento do Modelo**: a rede neural foi treinada usando
  [Keras](https://keras.io/) e
  [Scikit-learn](https://scikit-learn.org/stable/index.html);
- **Interatividade**: o usuário insere métricas anteriores do jogador para
  prever seu desempenho.

## Tecnologias Utilizadas

- **Python**: linguagem de programação utilizada;
- **Pandas**: para conversão de dados em formato CSV;
- **NumPy**: para manipulação de arrays;
- **Scikit-learn**: para divisão da base de dados entre teste e treinamento;
- **Keras**: para treinamento e teste de modelos de aprendizagem de máquina;
- **Flask**: para criação da página web.
