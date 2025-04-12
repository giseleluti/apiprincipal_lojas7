import os

import requests
from flask import Flask, request, redirect, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
# swagger specific ###
SWAGGER_URL = '/swagger/api'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Principal Lojas7"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# end swagger specific ###


# Configuração das URLs das APIs
API_URLS = {
    "produtos": os.environ.get("PRODUTOS", "http://127.0.0.1:5001"),
    "usuarios": os.environ.get("USUARIOS", "http://127.0.0.1:5002"),
    "pedidos": os.environ.get("PEDIDOS", "http://127.0.0.1:5003"),
    "APIPRINCIPAL": os.environ.get("APIPRINCIPAL", "http://127.0.0.1:5000")
}


# Dicionário para armazenar a contagem de requisições por endpoint
request_counts = {
    "usuarios": 0,
    "produtos": 0,
    "pedidos": 0
}


# Rota para redirecionar para a interface Swagger UI da API de usuários e incrementar o contador
@app.route('/usuarios')
@app.route('/usuarios/')
def redirect_usuarios_swagger():
    request_counts["usuarios"] += 1
    return redirect(f"{API_URLS['usuarios']}/swagger/")


# Rota para redirecionar para a interface Swagger UI da API de produtos e incrementar o contador
@app.route('/produtos')
@app.route('/produtos/')
def redirect_produtos_swagger():
    request_counts["produtos"] += 1
    return redirect(f"{API_URLS['produtos']}/apidocs/")


# Rota para redirecionar para a interface Swagger UI da API de pedidos e incrementar o contador
@app.route('/pedidos')
@app.route('/pedidos/')
def redirect_pedidos_swagger():
    request_counts["pedidos"] += 1
    return redirect(f"{API_URLS['pedidos']}/apidocs/")


# Rota para exibir a contagem de requisições
@app.route('/requests_count')
def get_requests_count():
    return jsonify(request_counts)


# Rota genérica para encaminhar outras requisições para as APIs de backend
@app.route('/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway(service, path):
    if service not in API_URLS:
        return "Serviço não encontrado", 404
    target_url = f"{API_URLS[service]}/{path}"
    headers = dict(request.headers)
    try:
        response = requests.request(
            method=request.method, url=target_url, headers=headers, params=request.args, json=request.get_json()
        )
        headers_response = dict(response.headers)
        headers_response.pop('Content-Length', None)
        headers_response.pop('Transfer-Encoding', None)
        return response.content, response.status_code, headers_response
    except requests.exceptions.RequestException as e:
        return f"Erro ao comunicar com o serviço '{service}': {e}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
