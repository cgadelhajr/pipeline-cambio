# pipeline-cambio

Este projeto implementa uma pipeline de dados responsavel por coletar, tranformar, validar e armarzenar cotações de moedas. 
Pipeline de dados do modulo M3 (NExT Dados 2026.1, CESAR School).

O fluxo realiza as seguintes etapas:
1. Consulta uma API de cotaçoes;
2. Salva a resposta em Json na Camada raw;
3. Transforma os dados em um DataFrame;
4. Padroniza nomes e tipos de colunas;
5. Valido a qualidade dos dados
6. Armazeno o histórico das cotações no PostgreSQL
7. Gera um resumo por moeda;
8. Armazena os documentos resumidos no MongoDB.

## Como rodar
1. Criar e ativar o venv
2. pip install -r requirements.txt
3. python src/pipeline.py

## Arquitetura da pipeline
![Diagrama da Arquitetura](./pipelinecambio.drawio.png)

## Decisões técnicas
1. Porque salvar o Json Bruto?
é a resposta salva original da API antes de transformar para preservar o dado recebido da fonte.

2. Validações Realizadas:

Antes de carregar os dados no banco a pipeline realiza validações para evitar o armazenamento de informações inconsistentes:

- DataFrame Vazio: 
- Colunas Obrigatórias
- Conversão de Tipo
- Valores Nulos e Inconsistes