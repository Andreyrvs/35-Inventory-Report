# Inventory Report

## Contexto

um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

Esses dados de estoque poderão ser obtidos de diversas fontes:

- Através da importação de um arquivo CSV;

- Através da importação de um arquivo JSON;

- Através da importação de um arquivo XML.

Além disso, o relatório final possuirá duas versões: simples e completa

## Técnologias usadas

Aplicação:

> Desenvolvido usando: Python

## Habilidades

Adquiri essas habilidades ao desenvolver esse projeto:

- Aplicar conceitos de Orientação a Objetos em Python;

- Aplicar padrões de projeto;

- Leitura e escrita de arquivos (XML, CSV, JSON).

## Instalando Dependências

- clone o projeto:

    ```bash
    git clone git@github.com:Andreyrvs/35-Inventory-Report.git
    ```

> Aplicação

1. **Entre no diretório**

    ```bash
    cd 35-Inventory-Report
    ```

2. **Criar o ambiente virtual**

    ```bash
    python3 -m venv .venv
    ```

3. **Ativar o ambiente virtual**

    ```bash
    source .venv/bin/activate
    ```

4. **Instalar as dependências no ambiente virtual**

    ```bash
    python3 -m pip install -r dev-requirements.txt
    ```

## Executando aplicação

- Para rodar a aplicação:

  ```bash
  cd src/
  python3 -u
  ```

## Executando Testes

- Para rodar todos os Testes:

  ```bash
  python3 -m pytest
  ```
