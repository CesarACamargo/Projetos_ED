# 🌤️ Pipeline ETL de Dados Climáticos com Apache Airflow e PostgreSQL

## 📌 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de Engenharia de Dados por meio da construção de um pipeline ETL automatizado para coleta, transformação e armazenamento de dados meteorológicos.

O pipeline realiza consultas periódicas à API OpenWeatherMap, transforma os dados recebidos e os armazena em um banco de dados PostgreSQL para posterior análise.

Este projeto foi reproduzido inicialmente para fins de aprendizado a partir do trabalho disponibilizado por Luiza Viana, servindo como base para compreender a integração entre Airflow, PostgreSQL, Docker e Python.

## 🙏 Créditos

Projeto original utilizado como referência:

* Repositório: https://github.com/vbluuiza/pipeline_etl_weather_data_tutorial_youtube
* Autora: Luiza Viana

Todo o crédito pela concepção e implementação original pertence à autora. Este repositório representa minha reprodução prática do projeto como parte dos meus estudos em Engenharia de Dados.

## 🎯 Objetivos de Aprendizagem

Durante o desenvolvimento deste projeto busquei praticar:

* Construção de pipelines ETL
* Orquestração de workflows com Apache Airflow
* Integração entre containers Docker
* Consumo de APIs REST
* Manipulação de dados com Pandas
* Persistência de dados em PostgreSQL
* Organização de projetos Python
* Utilização de ambientes virtuais

## 🛠️ Tecnologias Utilizadas

### Linguagem

* Python 3.11.15

### Orquestração

* Apache Airflow

### Banco de Dados

* PostgreSQL (Docker)

### Containerização

* Docker
* Docker Compose

### Bibliotecas

* Pandas
* Requests
* SQLAlchemy
* Psycopg2
* Python-dotenv

### Ferramentas de Desenvolvimento

* Visual Studio Code (VS Code)
* Git
* GitHub

## 💻 Ambiente Utilizado

### Sistema Operacional

* openSUSE Leap 15.6

### Infraestrutura Local

A aplicação foi executada localmente utilizando containers Docker para os serviços de banco de dados e orquestração.

Estrutura utilizada:

* Container PostgreSQL (postgres:latest)
* Container Apache Airflow
* Ambiente virtual Python dedicado ao projeto

## 🚀 Passos Executados

Para reproduzir o ambiente realizei as seguintes etapas:

### 1. Configuração do Banco de Dados

* Instalação do PostgreSQL utilizando a imagem `postgres:latest` via Docker.

### 2. Configuração do Apache Airflow

* Instalação do Apache Airflow em container Docker.
* Configuração da comunicação entre o Airflow e o container PostgreSQL.

### 3. Configuração do Ambiente Python

* Criação de ambiente virtual Python 3.11.15.
* Instalação das dependências necessárias para execução do pipeline.

### 4. Desenvolvimento e Execução

* Utilização do Visual Studio Code para edição dos scripts Python.
* Configuração da DAG responsável pela execução automática das etapas de extração, transformação e carga.

## ⚠️ Principais Desafios Encontrados

O principal desafio durante a implementação foi estabelecer a comunicação entre o container do Apache Airflow e o container PostgreSQL.

Para resolver esse problema foi necessário compreender:

* Redes Docker
* Resolução de nomes entre containers
* Configuração correta das strings de conexão
* Mapeamento de portas
* Variáveis de ambiente utilizadas pelo Airflow

Essa etapa foi importante para consolidar conhecimentos sobre infraestrutura containerizada.

## 📚 Aprendizados

Através deste projeto adquiri experiência prática em:

* Conceitos de ETL (Extract, Transform, Load)
* Criação e execução de DAGs no Airflow
* Integração entre múltiplos containers Docker
* Consumo de APIs externas
* Transformação de dados utilizando Pandas
* Persistência de dados em PostgreSQL
* Configuração de ambientes Python para projetos de dados
* Estruturação de projetos de Engenharia de Dados

Além dos aspectos técnicos, o projeto permitiu compreender melhor o fluxo completo de ingestão e processamento de dados utilizado em ambientes reais de Engenharia de Dados.

## 🔮 Próximas Melhorias

- Coletar dados de múltiplas cidades brasileiras
- Implementar validações de qualidade de dados
- Criar dashboard para visualização dos dados
- Adicionar testes automatizados
- Implementar monitoramento e alertas do pipeline
