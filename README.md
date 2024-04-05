# Sistema que permite ao usuário visualizar os logs de acesso a duas rotas

- '/ping': Requisição do tipo GET, que deve retornar um JSON {'resposta': 'pong'};
- '/echo': Requisição do tipo POST, que deve retornar um JSON com o seguinte formato - {'resposta': 'o que o usuário enviou'}. Os dados de entrada devem ter o seguinte formato {'dados': 'texto'}.

## Setup

1. Ensure Python 3.8 or newer is installed on your system.
2. Clone this repository to your local machine.
3. Install the required Python packages by running `pip install -r requirements.txt` in the project root directory.

## Running the Application

1. Navigate to the project root directory in your terminal.
2. Run the Flask application with `python -m flask run`.
3. Open a web browser and go to `http://127.0.0.1:5000/` to access the web interface.

## Creating VENV

1. `python -m venv venv`
2. `source venv/bin/activate`
