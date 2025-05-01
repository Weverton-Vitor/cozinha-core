# Cozinha Core

Cozinha Core é um projeto Python que pode ser instalado como um módulo e executado a partir de um entrypoint.

## Índice

1. [Requisitos](#requisitos)
2. [Instalação e Execução](#instalação-e-execução)
   - [Criar um Ambiente Virtual](#1-criar-um-ambiente-virtual-opcional-mas-recomendado)
   - [Instalar Dependências](#2-instalar-dependências)
   - [Executar o EntryPoint](#3-executar-o-entrypoint)
3. [Documentação](#documentação)
4. [Contribuição](#contribuição)

## Requisitos

- Python 3.11+
- `pip` e `venv` configurados corretamente

## Instalação e Execução

### 1. Criar um Ambiente Virtual (Opcional, mas Recomendado)

Se estiver executando o projeto em uma máquina pessoal, crie um ambiente virtual:

```sh
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate    # Windows
```

### 2. Instalar Dependências

Instale as dependências definidas no `pyproject.toml` e o próprio projeto:

```sh
pip install .
```

### 3. Executar o EntryPoint

Para rodar o projeto, utilize o comando:

```sh
python3 python -m entrypoints.main
```

Caso tenha problemas ao executar o entrypoint, verifique se o ambiente virtual está ativado e se o módulo foi instalado corretamente.

## Documentação

Para acessar os diagramas de casos de uso e UML, clique no link abaixo:

[Diagramas de Casos de Uso e UML](https://drive.google.com/file/d/1EUKeUfs_wPolLmFyQ0JzhjZTxH-UK5Gt/view?usp=sharing)

## Contribuição

Sinta-se à vontade para abrir issues e contribuir com melhorias para o projeto!
