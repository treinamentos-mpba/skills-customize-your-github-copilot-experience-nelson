# 📘 Tarefa: Testes e Depuração em Python

## 🎯 Objective

Aprenda a usar o módulo `unittest` para verificar funções Python, identificar casos-limite e corrigir defeitos com base nos resultados dos testes. Você vai testar um pequeno gerenciador de tarefas usando o arquivo inicial fornecido.

## 📝 Tasks

### 🛠️ Testar a criação e a conclusão de tarefas

#### Descrição
Crie `test_task_manager.py` e escreva testes automatizados para as funções `add_task` e `complete_task` do módulo `task_manager.py`. Execute os testes com `python -m unittest -v` e use os resultados para investigar o comportamento do programa.

#### Requisitos
O programa concluído deve:

- Usar `unittest.TestCase` e métodos de teste com nomes iniciados por `test_`
- Verificar se `add_task` inclui uma tarefa com ID, título e estado inicial `completed` igual a `False`
- Verificar se `complete_task` retorna `True` e marca a tarefa existente como concluída, ou retorna `False` quando o ID não existe


### 🛠️ Testar entradas e casos-limite

#### Descrição
Amplie a suíte com testes para títulos vazios ou com espaços e para a criação de tarefas quando os IDs existentes não são consecutivos. Use os testes que falharem para corrigir `add_task`.

#### Requisitos
O programa concluído deve:

- Rejeitar um título vazio ou composto apenas por espaços com `ValueError`
- Remover espaços extras do início e do fim de um título válido
- Gerar um ID que não esteja em uso, mesmo quando uma tarefa anterior foi removida da lista
- Manter todos os testes anteriores aprovados após as correções


### 🛠️ Testar a busca e depurar o gerenciador

#### Descrição
Escreva testes para `find_task`, corrija os defeitos encontrados e execute novamente toda a suíte. A busca deve encontrar o título independentemente de diferenças entre letras maiúsculas e minúsculas.

#### Requisitos
O programa concluído deve:

- Retornar a tarefa correspondente quando o título buscado existe, sem diferenciar maiúsculas de minúsculas
- Retornar `None` quando não houver uma tarefa com o título buscado
- Passar todos os testes com `python -m unittest -v`
- Usar os testes para reproduzir e verificar cada correção, sem remover testes para ocultar falhas
