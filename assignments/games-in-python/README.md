# 📘 Assignment: Hangman in Python

## 🎯 Objective

Pratique strings, listas, loops, condicionais e entrada de dados em Python criando uma versão jogável do Jogo da Forca.

## 📝 Tasks

### 🛠️ Preparar a Palavra e Exibir o Progresso

#### Descrição
Use a lista de palavras fornecida no código inicial para escolher aleatoriamente uma palavra secreta. Mostre ao jogador o progresso da palavra oculta e atualize-o conforme as letras forem adivinhadas.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida.
- Exibir uma posição para cada letra ainda não adivinhada, no formato `_ _ _`.
- Solicitar palpites de letras e revelar todas as posições correspondentes quando a letra estiver na palavra.

### 🛠️ Controlar as Tentativas e Encerrar o Jogo

#### Descrição
Implemente o loop principal do jogo para acompanhar os palpites incorretos e encerrar a partida quando o jogador adivinhar a palavra ou atingir o limite de erros.

#### Requisitos
O programa concluído deve:

- Contar e exibir as tentativas incorretas restantes, usando um limite máximo definido no programa.
- Continuar o jogo enquanto a palavra não for descoberta e ainda houver tentativas.
- Encerrar com uma mensagem de vitória quando todas as letras da palavra forem adivinhadas.
- Encerrar com uma mensagem de derrota e revelar a palavra secreta quando as tentativas incorretas se esgotarem.
