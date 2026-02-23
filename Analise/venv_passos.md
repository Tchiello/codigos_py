# Passo a passo para criar um venv

1. **Criar a pasta do projeto**
   - No terminal, navegue até o local desejado e crie a pasta:
     - `mkdir MeuProjeto`
     - `cd MeuProjeto`

2. **Criar o ambiente virtual (venv)**
   - Execute:
     - `python -m venv venv`

3. **Ativar o venv**
   - No Windows (PowerShell):
     - `venv\Scripts\Activate`
   - No Windows (CMD):
     - `venv\Scripts\activate.bat`

4. **Confirmar a ativação**
   - Verifique se o prompt exibiu `(venv)` no início.

5. **Atualizar o pip (opcional, recomendado)**
   - `python -m pip install --upgrade pip`

6. **Instalar dependências (se necessário)**
   - `pip install <pacote>`

7. **Registrar dependências em um arquivo**
   - `pip freeze > requirements.txt`

8. **Desativar o venv**
   - `deactivate`

---

## Observações
- Substitua `MeuProjeto` pelo nome real da sua pasta.
- O nome `venv` é um padrão, mas pode ser alterado.
