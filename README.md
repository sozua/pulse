
# Pulse

![App Screenshot](/assets/logo.png)

Pulse é uma API simples para o gerenciamento de consultas médicas utilizando Django e Django Rest Framework


## Rodando localmente

```bash
# Clone o projeto
git clone https://github.com/sozua/pulse.git

# Acesse o diretório do projeto
cd pulse

# Crie um ambiente virtual para o python
python3 -m venv .venv
# Ative o ambiente virtual em seu terminal

source ./.venv/bin/activate
# Instale as dependencias
pip install -r requirements.txt

# Crie as migrations
python3 manage.py makemigrations
# Execute as migrations
python3 manage.py migrate --run-syncdb

# Rode os testes
python3 manage.py test
# Caso queira, inicie o servidor
python3 manage.py runserver
```
## Stack utilizada

- Django
- Django Rest Framework
- Pylint


## Documentação da API
Para acessar a documentação do projeto,  utilize a seguinte rota:
```http
  GET http://localhost:8000/swagger
```