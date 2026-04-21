#Excel to ClickUp Automation 

Automação em Python para ler projetos de uma planilha Excel e criar tarefas automaticamente em ClickUp via API.

##Visão Geral

Este projeto foi desenvolvido para reduzir trabalho manual no cadastro de tarefas operacionais.

Fluxo:
Excel -> Python -> ClickUp API

A aplicação lê uma planilha com projetos pendentes e cria tarefas automaticamente em uma lista do ClickUp.

##Problema Resolvido

Em muitos times, demandas chegam por planilhas e precisam ser cadastradas manualmente em ferramentas de gestão.
Esse projeto automatiza esse processo, trazendo:

- ganho de produtividade
- redução de erros manuais
- padronização operacional
- escalabilidade

##Tecnologias Utilizadas

- Python 3.x
- Pandas
- OpenPyXL
- Requests
- ClickUp API

#Como Executar?

1. Instalar as dependências: pip install -r requirements.txt

2. Configurar as credenciais no arquivo config.py: CLICKUP_TOKEN e LIST_ID

3. Executar o projeto: python main.py


Autor
Juan Domingues
