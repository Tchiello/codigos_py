# Como criar um Notebook Jupyter

## 1) (Opcional) Criar e ativar um venv
- Crie a pasta do projeto e entre nela:
  - `mkdir MeuProjeto`
  - `cd MeuProjeto`
- Crie o ambiente virtual:
  - `python -m venv venv`
- Ative o venv:
  - PowerShell: `venv\Scripts\Activate`
  - CMD: `venv\Scripts\activate.bat`

## 2) Instalar o Jupyter
- `python -m pip install --upgrade pip`
- `pip install notebook`

## 3) Criar e abrir um Notebook
- Inicie o servidor do Jupyter:
  - `jupyter notebook`
- No navegador, clique em **New** → **Python 3**.
- O arquivo será criado com extensão `.ipynb`.

## 4) Salvar o Notebook
- Use **File** → **Save and Checkpoint** (ou `Ctrl+S`).

---

## Observações
- O comando `jupyter notebook` abre o painel no navegador.
- Você pode criar quantos notebooks quiser no mesmo projeto.
