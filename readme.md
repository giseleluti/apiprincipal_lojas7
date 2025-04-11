# API Gateway Principal

Este projeto implementa um API Gateway principal em Python utilizando Flask e Docker Compose, projetado para integrar três APIs Python com Swagger.

## Funcionalidades

* **Agregação de APIs:** O API Gateway atua como um ponto de entrada único para todas as três APIs, simplificando o acesso e o gerenciamento através de redirecionamento.
* **Contagem de Requests por Endpoint:** Além disso, oferece um endpoint para monitorar o número de acessos à documentação de cada uma dessas APIs.
* **Documentação Swagger:** Fornece acesso à documentação Swagger das APIs Python através de rotas dedicadas.
* **Orquestração com Docker Compose:** Facilita a implantação e o gerenciamento de todos os serviços (API Gateway e APIs) utilizando Docker Compose.

## Requisitos Mínimos para Execução

* **Docker:** Certifique-se de que o Docker esteja instalado e em execução em seu sistema.
* **Docker Compose:** Certifique-se de que o Docker Compose esteja instalado em seu sistema.
* **APIs Dependentes:** As três APIs devem estar disponíveis em um diretório raiz.
* **Python:** Versão 3.9 ou superior instalada.
* **Pip:** Gerenciador de pacotes do Python instalado.

## Detalhamento das Rotas

1. **Redirecionamento para a Documentação Swagger das APIs Python:**
   * `/usuarios` -> Redireciona para a Swagger UI da API de Usuários (`/swagger/`).
   * `/produtos` -> Redireciona para a Swagger UI da API de Produtos (`/apidocs/`).
   * `/pedidos` -> Redireciona para a Swagger UI da API de Pedidos (`/apidocs/`).

2. **Servir a Documentação Swagger da Própria API Gateway:**
   * A interface Swagger UI para documentar a própria API Principal está disponível em `/swagger/api`.
   * Você poderá utilizar o ponto de entrada dela para acessar na `descrição` os endpoints oficiais de cada serviço.
   * A especificação da API Gateway é servida em `/static/swagger.json`.

3. **Contagem de Acessos à Documentação:**
   * Mantém uma contagem do número de vezes que os endpoints `/usuarios`, `/produtos` e `/pedidos` foram acessados para visualização da documentação.
   * Essa contagem pode ser consultada através do endpoint `GET /requests_count`.

4. **Proxy Genérico para APIs de Backend:**
   * Fornece uma rota genérica em `/<service>/<path:path>` para encaminhar requisições (GET, POST, PUT, DELETE) para as APIs de backend subjacentes. Isso permite que a API Gateway atue como um ponto de entrada para outras funcionalidades das APIs, embora atualmente o foco principal seja a documentação.

## Imagem das APIS integradas:
graph TD
    subgraph Lojas7
        A[API Principal] --> B(API de Usuários);
        A --> C(API de Produtos);
        A --> D(API de Pedidos);

        B -- Autentica, Valida Dados, Persiste Dados, Simula Login --> B;

        C -- Integração --> E[FakeStore API (Externa)];
        C -- Cache de Produtos --> D;

        D -- Cadastra Pedidos --> D;

        style A fill:#f9f,stroke:#333,stroke-width:2px
        style B fill:#ccf,stroke:#333,stroke-width:2px
        style C fill:#9cf,stroke:#333,stroke-width:2px
        style D fill:#fcc,stroke:#333,stroke-width:2px
        style E fill:#eee,stroke:#333,stroke-width:2px
    end

## Execução

1. **Clone os 4 Repositórios e navegue para a pasta da API Principal:**

   ```bash
   git clone <URL_DO_REPOSITORIO_PRINCIPAL>
   cd apiprincipal_lojas7
Observação: Assumindo que você também clonou os repositórios das APIs de usuários, produtos e pedidos no mesmo diretório pai ou em um local acessível.
2. 
Construa e Execute os Containers com Docker Compose:
Bash
Copiar o código
docker-compose up --build
Este comando irá construir as imagens Docker e iniciar os containers definidos no arquivo docker-compose.yml.
3. 
Acesse o API Gateway com a Documentação Swagger:
O API Gateway estará disponível em http://localhost:5000/swagger/api.
4. 
Acesse a Documentação Swagger das APIs Python:
• API de Produtos: http://localhost:5000/produtos
• API de Usuários: http://localhost:5000/usuarios
• API de Pedidos: http://localhost:5000/pedidos
5. 
Acesse os Endpoints das APIs Diretamente (Sem passar pelo Gateway para dados):
Para acessar os endpoints das APIs diretamente (sem o proxy genérico do gateway), utilize as seguintes URLs (assumindo que as APIs estão rodando nas portas padrão):
http://localhost:5001/apidocs/  (API de Produtos)
http://localhost:5002/swagger    (API de Usuários)
http://localhost:5003/apidocs/  (API de Pedidos)
Configuração
• URLs das APIs: As URLs das APIs backend que o gateway proxy está configurado para usar estão definidas no arquivo app.py. Certifique-se de ajustá-las de acordo com a configuração da sua rede Docker no docker-compose.yml.
• Arquivo docker-compose.yml: Este arquivo define os serviços (API Gateway e as APIs backend) e a rede para os containers Docker. Ajuste as configurações de portas, volumes e dependências conforme necessário.
• Dockerfiles das APIs: Os Dockerfiles das APIs estão localizados nos diretórios correspondentes de cada API. Certifique-se de que estejam configurados corretamente para construir as imagens das APIs.