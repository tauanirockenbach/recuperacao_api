##Consumo de API
##tem como base usar consumir uma API já disponivel para consumo

#Instalação e configuração:
Deve ser instalada localmente, logo, é necessário a instalação do python(Utilizado = VS code) e Git para fazer o versionamento.

Criar o ambiente virtual:
python -m venv .venv

Ativar o ambiente virtual:
.\.venv\Scripts\Activate.ps1

Instalar as dependências:
pip install -r requirements.txt

Executar a API:
uvicorn app.main:app --reload (Ele precisa ficar ligado para bom funcionamento caso contrário ele não irá rodar)

Endpoint de consulta: http://127.0.0.1:8000/v1/forecast


