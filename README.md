<div align="center">
  <h1>🍷 MLOps Previsão de Qualidade de Vinho</h1>
  <p>Um pipeline de Machine Learning ponta a ponta para previsão da qualidade do vinho com práticas de MLOps.</p>

  [![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
  [![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![MLflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=flat&logo=mlflow&logoColor=blue)](https://mlflow.org/)
  [![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
</div>

<hr />

## Visão Geral

**MLOps Previsão de Qualidade de Vinho** é um pipeline de Machine Learning ponta a ponta, robusto e escalável, projetado para prever a qualidade do vinho com base em suas propriedades físico-químicas.
Construído com foco em produção, este projeto demonstra os princípios fundamentais de MLOps, abrangendo desde a ingestão de dados até o deploy do modelo usando uma interface web interativa.

## Funcionalidades

- **Pipeline Ponta a Ponta:** Estágios automatizados para Ingestão, Validação, Transformação de Dados, Treinamento e Avaliação do Modelo.
- **Rastreamento de Experimentos:** Integrado com MLflow para rastrear parâmetros, métricas e modelos.
- **Interface Web:** Uma aplicação web Flask elegante para fazer previsões de forma dinâmica.
- **Design Modular:** Componentes estruturados e gerenciamento de configuração usando YAML.
- **Arquitetura Extensível:** Fácil substituição de conjuntos de dados, modelos e alvos de deploy.

## Arquitetura

O pipeline é composto pelos seguintes estágios sequenciais:

1. **Ingestão de Dados:** Baixa e extrai o conjunto de dados no ambiente local.
2. **Validação de Dados:** Verifica o esquema de dados e garante que todas as colunas e tipos necessários estejam presentes.
3. **Transformação de Dados:** Limpa, normaliza e prepara os dados para o treinamento, dividindo-os em conjuntos de treino e teste.
4. **Treinamento do Modelo:** Treina um modelo de machine learning nos dados processados.
5. **Avaliação do Modelo:** Avalia o modelo usando métricas e registra os resultados.

## Começando

### Pré-requisitos

- Python 3.10 ou superior
- Git

### Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/ramoneirao/mlops-wine-prediction.git
   cd mlops-wine-prediction
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows use: .venv\Scripts\activate
   ```

3. **Instale as dependências**
   As dependências são gerenciadas via `pyproject.toml` ou `uv`:
   ```bash
   pip install -e .
   ```

## Uso

### 1. Treinando o Pipeline

Você pode executar o pipeline de ML completo do início ao fim com o comando:

```bash
python main.py
```
Isso executará todos os estágios e salvará o modelo treinado e as métricas em seus respectivos diretórios (`artifacts/`).

### 2. Executando a Aplicação Web

Para iniciar a aplicação web Flask e interagir com o modelo:

```bash
uv run app.py
```
Em seguida, abra seu navegador e acesse `http://localhost:8080`.
Você também pode acionar uma execução de treinamento diretamente pela API em `http://localhost:8080/train`.

## Estrutura do Projeto

```text
mlops-wine-prediction/
├── config/             # Arquivos YAML de configuração
├── src/                # Pacote principal do código-fonte
│   └── mlops_wine_prediction/
│       ├── components/ # Lógica dos estágios do pipeline
│       ├── config/     # Gerenciadores de configuração
│       ├── entity/     # Classes de dados para configurações
│       └── pipeline/   # Orquestradores do pipeline
├── static/             # Arquivos estáticos para a aplicação web (CSS, JS)
├── templates/          # Templates HTML para a aplicação web
├── artifacts/          # Conjuntos de dados gerados, modelos e métricas
├── mlruns/             # Diretório de rastreamento do MLflow
├── app.py              # Ponto de entrada da Aplicação Web Flask
├── main.py             # Script de execução do pipeline
└── pyproject.toml      # Metadados e dependências do projeto
```

## Fluxo de Trabalho MLOps

Para estender ou modificar o pipeline, siga estas etapas padrão:
1. Atualize `config/config.yaml`
2. Atualize `schema.yaml`
3. Atualize `params.yaml`
4. Atualize a entidade (em `src/mlops_wine_prediction/entity`)
5. Atualize o gerenciador de configuração (em `src/mlops_wine_prediction/config`)
6. Atualize os componentes (em `src/mlops_wine_prediction/components`)
7. Atualize o pipeline (em `src/mlops_wine_prediction/pipeline`)
8. Atualize `main.py` se estiver adicionando novos estágios

