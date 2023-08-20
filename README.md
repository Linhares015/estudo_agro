# Estudo sobre o Agronegócio Brasileiro

Projeto: Desenvolvimento de um pipeline e de análise de dados para explorar tendências, produções e correlações no agronegócio brasileiro com fatores socioeconômicos e ambientais.

## Etapas de Desenvolvimento

1. **Extração de Dados**:
    - Extração de dados do IBGE Agricultura e outras fontes socioeconômicas.
    - Utilização da biblioteca `pandas` para importação e navegação inicial dos dados.

2. **Modelagem com dbt**:
    - Utilização do `dbt` para modelagem e transformação dos dados.
    - Enriquecimento dos dados através da combinação de múltiplas fontes.
    - Criação de modelos, testes e documentação.

3. **Carregamento no Google BigQuery**:
    - Utilização da biblioteca `google-cloud-bigquery` para carregar os dados transformados no BigQuery.
    - Estruturação dos dados em tabelas.

4. **Orquestração com Airflow**:
    - Configuração do Apache Airflow para orquestrar o pipeline de dados.
    - Criação de DAGs para automação e agendamento das tarefas.

## Protótipo do Pipeline

![Pipeline](https://media.licdn.com/dms/image/D4D22AQE_Rf0SFS-pMg/feedshare-shrink_1280/0/1691353538995?e=1694649600&v=beta&t=_EgvKfqvGHxNZccroxbDVdiSuUDX2DxAOnsJQmyspkQ)

## Passo a Passo

Utilizando o `dbt` e Python, os dados são extraídos, transformados e enriquecidos. Posteriormente, são carregados no Google BigQuery para análises mais profundas e visualizações. O Apache Airflow é utilizado para orquestrar todo o processo, garantindo que o pipeline seja executado de forma eficiente e em intervalos regulares.
O Power BI será utilizado para visualização dos dados.

## Sobre o Desenvolvedor

Tiago Linhares: Um louco por conhecimento, apaixonado por tecnologia e dados.

Conheça mais detalhes no [LinkedIn](https://www.linkedin.com/in/tiago-linhares/).

Fique à vontade para se conectar nas redes sociais:

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tiago-linhares/)

[![Blog LinharesCorp](https://img.shields.io/badge/-LinharesCorp%20Blog-%230077B5?style=for-the-badge&logo=blogger&logoColor=white)](https://www.linharescorp.com/blog)
