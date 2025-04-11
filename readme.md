# API Gateway Principal

Este projeto implementa um API Gateway principal em Python utilizando Flask e Docker Compose, projetado para integrar três APIs  Python com Swagger .

## Funcionalidades

* **Agregação de APIs:** O API Gateway atua como um ponto de entrada único para todas as três APIs, simplificando o acesso e o gerenciamento através de redirecionamento.
* **contagem de requestes por endpoints: ** Além disso, ela oferece um endpoint para monitorar o número de acessos à documentação de cada uma dessas APIs.
* **Documentação Swagger:** Fornece acesso à documentação Swagger das APIs Python através de rotas dedicadas.
* **Orquestração com Docker Compose:** Facilita a implantação e o gerenciamento de todos os serviços (API Gateway e APIs) utilizando Docker Compose.

## Requisitos Mínimos para Execução

* **Docker:** Certifique-se de que o Docker esteja instalado e em execução em seu sistema.
* **Docker Compose:** Certifique-se de que o Docker Compose esteja instalado em seu sistema.
* **APIs Dependentes:** As três APIs  devem estar disponíveis e em um diriretório raiz.
* ** python instalado ** Versão a partir da 3.9.
* **pip** (gerenciador de pacotes do Python)

## detalhamento das rotas:
    * `/usuarios` -> Redireciona para a Swagger UI da API de Usuários (`/swagger/`).
    * `/produtos` -> Redireciona para a Swagger UI da API de Produtos (`/apidocs/`).
    * `/pedidos` -> Redireciona para a Swagger UI da API de Pedidos (`/apidocs/`).

2.  **Servir a Documentação Swagger da Própria API Gateway:**
    * A interface Swagger UI para documentar a própria API Principal está disponível em `/swagger/api`.
    * Você poderá utilizar o ponto de entrada dela para acessar na `descrição`os endpoints oficiais de cada serviço.
    * A especificação da API Gateway é servida em `/static/swagger.json`.

3.  **Contagem de Acessos à Documentação:**
    * Mantém uma contagem do número de vezes que os endpoints `/usuarios`, `/produtos` e `/pedidos` foram acessados para visualização da documentação.
    * Essa contagem pode ser consultada através do endpoint GET `/requests_count`.

4.  **Proxy Genérico para APIs de Backend:**
    * Fornece uma rota genérica em `/<service>/<path:path>` para encaminhar requisições (GET, POST, PUT, DELETE) para as APIs de backend subjacentes. Isso permite que a API Gateway atue como um ponto de entrada para outras funcionalidades das APIs, embora atualmente o foco principal seja a documentação.

## Execução

1.  **Clone os 4 Repositórios e navegue para a api principal:**

    ```bash
    cd apiprincipal_lojas7
    ```

2.  **Construa e Execute os Containers com Docker Compose:**

    ```bash
    docker-compose up --build
    ```

    Este comando irá construir as imagens Docker  e iniciar os containers definidos no arquivo `docker-compose.yml`.

3.  **Acesse o API Gateway com documentação swagger:**

    O API Gateway estará disponível em `http://localhost:5000/swagger/api`.

4.  **Acesse a Documentação Swagger das APIs Python:**

    * API de produtos: `http://localhost:5000/produtos`
    * API de usuários: `http://localhost:5000/usuarios`
    * API  de pedidos: `http://localhost:5000/pedidos`

5.  **Acesse os Endpoints das APIs:**

    Para acessar os endpoints das APIs sem passar pela api principal, utilize a seguinte estrutura de URL:

    ```
    http://localhost:5001/apidocs/
    http://localhost:5002/swagger
    http://localhost:5003/apidocs/
```

    
## Configuração

* **URLs das APIs:** As URLs das APIs estão definidas no arquivo `app.py`. Certifique-se de ajustá-las de acordo com a configuração da sua rede Docker.
* **Arquivo `docker-compose.yml`:** Este arquivo define os serviços e a rede para os containers Docker. Ajuste as configurações conforme necessário.
* **Dockerfile das APIs:** Os Dockerfiles das APIs estão localizados nos diretórios correspondentes. Certifique-se de que estejam configurados corretamente.

