<h1 align="center" style="font-weight: bold;"> API Rest Python desenvolvida utilizando TDD 💻</h1>

<div align="center">

![python][PYTHON__BADGE]
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

</div>

<p align="center">
 <a href="#tdd">TDD</a> •
 <a href="#started">Como começar</a> •
 <a href="#routes">API Endpoints</a> •
 <a href="#author">Autor</a> •
 <a href="#referencias">Referencias</a> •
</p>

<p align="center">
  <b>Construindo uma Api rest async com python usando TDD (Test Driven Development) no bootcamp Python AI Backend Developer da DIO</b>
</p>

<h2 id="tdd">✅ Test Driven Development </h2>
TDD é a sigla para Test Driven Development, que em português significa Desenvolvimento Orientado por Testes. Esse é um método de desenvolvimento de software que se concentra em escrever testes automatizados antes de escrever o código. Essa abordagem ajuda os desenvolvedores a identificar e corrigir bugs mais rapidamente, além de garantir que o código atenda aos requisitos do projeto

A imagem abaixo mostra como funciona o ciclo do TDD.

![tdd](docs/imgs/tdd.png)

para saber mais sobre o TDD acesse os link na sessão de <a id="referencias">referencias</a>

<h2 id="started">🚀 Como começar</h2>

Para começar, siga as etapas abaixo

<h3> Tech Stack </h3>

- Python
- Fastapi
- Uvicorn
- Pydantic
- MongoDB
- Docker

<h3>Clonar</h3>

Como clonar este projeto

```bash
git clone https://github.com/duca-meneses/store_api.git
```

Depois de clonar o projeto

```bash
poetry install
```

se você não usa poetry

crie um ambiente virtual

```bash
python -m venv .venv
```

Ative seu ambiente virtual (.venv) no Windows

```bash
.venv/Scripts/activate
```

Ative seu ambiente virtual (.venv) no Linux/mac

```bash
source .venv/bin/activate
```

Agora, execute o comando para instalar as dependências do projeto

```bash
pip install -r requirements.txt
```

<h3>Starting</h3>

Para iniciar o servidor uvicorn para roda a aplicação FastAPI.

```bash
make run
```

Para rodar todos testes da aplicação:

```bash
make test
```

Para rodar test específicos:

```bash
make test-matching K=O_nome_do_test
```

<h2 id="routes">📍 API Endpoints</h2>

Aqui esta a lista das principais rotas da API e quais são os corpos de solicitação esperados.

![endpoints](docs/imgs/image.png)

para acessar o Swagger da aplicação

http://localhost:8000/docs

<h2 id="author">Autor</h2>

<table
  >
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/53846394?v=4" width="100px;" alt="Carlos Eduardo Profile Picture"/><br>
        <sub>
          <b>Carlos Eduardo</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2 id="referencias">📖 Referencias</h2>

O repositório do projeto da dio: https://github.com/digitalinnovationone/store_api

FastAPI: https://fastapi.tiangolo.com/

Pydantic: https://docs.pydantic.dev/latest/

TDD: https://dev.to/womakerscode/o-que-e-tdd-4b5f#:~:text=TDD%20significa%20Desenvolvimento%20Orientado%20por,do%20XP%20(Extreme%20Programming).

[PYTHON__BADGE]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
