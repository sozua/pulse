
# Pulse

![App Screenshot](https://gist.github.com/sozua/de4d7070588771733b416101f798c80f/raw/cee38d5b76898ddfef22ed3f7129b707610f0e63/logo.png)

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

# Inicie o servidor
python3 manage.py runserver
# Ou se preferir, rode os testes
python3 manage.py test
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