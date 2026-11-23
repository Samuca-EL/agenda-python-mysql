# Agenda de Contatos — Python + MySQL

Aplicação de terminal para cadastrar e consultar contatos, com os dados guardados em um banco MySQL.

Projeto desenvolvido na disciplina **Paradigmas de Linguagem com Python**, com o desafio de aplicar conceitos do **paradigma funcional** e de **modularizar a conexão com o banco de dados**.

## Funcionalidades

- Cadastrar contato (nome, telefone e e-mail)
- Listar todos os contatos
- Buscar contatos pelo nome (busca parcial com `LIKE`)
- Validação das entradas antes de gravar no banco

## Tecnologias

- Python 3
- MySQL
- mysql-connector-python
- PyInstaller (para gerar o executável)

## Conceitos aplicados

- **Paradigma funcional:** as funções recebem tudo o que precisam por parâmetro (inclusive a conexão) e devolvem um resultado, sem depender de variáveis globais.
- **Modularização:** a conexão fica no módulo `conexao.py`, que recebe o nome do banco como parâmetro e pode ser reutilizado em outros projetos.
- **CRUD com SQL:** `INSERT` e `SELECT` executados pelo cursor do conector.
- **Menu com `while` e `match/case`.**

## Estrutura

```
├── agenda.py            programa principal (menu e funções)
├── conexao.py           módulo de conexão com o MySQL
├── validacao.py         validação dos textos digitados
├── agenda.sql           script de criação do banco
├── config_exemplo.py    modelo do arquivo de configuração
└── requirements.txt
```

## Como executar

1. Crie o banco executando o `agenda.sql` no MySQL.
2. Copie `config_exemplo.py` para `config.py` e coloque o usuário e a senha do seu MySQL.
3. Crie o ambiente virtual e instale as dependências:

```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

4. Execute:

```
python agenda.py
```

### Gerar o executável (opcional)

```
pip install pyinstaller
pyinstaller --onefile --name agenda agenda.py
```

O arquivo `agenda.exe` é criado na pasta `dist`.

## Próximos passos

- Usar consultas parametrizadas (`%s`) no lugar de f-strings no SQL.
- Tratar erros de conexão com `try/except`.
- Adicionar edição e exclusão de contatos.
