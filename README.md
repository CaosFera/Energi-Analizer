<div align="center">
    <img src="assets/Energi-Analizer.png" alt="Logo Energi Analizer" width="500"/>
</div>


![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=Firefox-Browser&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)


<div style="text-align: justify;">
    <h4> 
        Energi Analyzer** é um projeto desenvolvido como parte de uma residência em software organizada pelo CEPEI. Este projeto foi criado para atender ao desafio de **Otimização Energética Inteligente na Indústria 4.0**, proposto em um hackathon. Nossa equipe escolheu este tema visando criar uma solução eficiente para o monitoramento e manutenção da iluminação pública.
    </h4>
</div>

## Objetivo do Projeto

O Energi Analyzer é uma ferramenta de monitoramento e gestão de lâmpadas em postes de iluminação pública, com foco em otimizar a eficiência energética e o processo de manutenção. Nosso objetivo é garantir que as lâmpadas estejam sempre operando de maneira ideal, minimizando custos e tempo de resposta em caso de falhas.

## Funcionalidades

- **Mapeamento Geográfico**: Registra e organiza todos os postes de iluminação com base em suas coordenadas geográficas, permitindo uma visão geral de cada ponto de luz.
- **Monitoramento Contínuo**: Monitora o status de cada lâmpada em tempo real, identificando rapidamente falhas ou irregularidades.
- **Relatórios Periódicos**: Gera relatórios regulares sobre o desempenho e o estado de cada poste, fornecendo dados para manutenção preditiva.
- **Eficiência na Manutenção**: A plataforma sugere ações de manutenção de acordo com o estado das lâmpadas, garantindo maior precisão e eficiência na reposição ou conserto das lâmpadas defeituosas.







<h2 align="center"> 
    :construction:  Projeto em construção  :construction:
</h2>
### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina Python 3.10 ou qualquer versão acima. Além disso, é bom ter um editor para trabalhar com o código, como [VSCode](https://code.visualstudio.com/).

### 🎲 Rodando o Back End (servidor)

```bash
# Clone este repositório
$ git clone https://github.com/CaosFera/FASHION-AVENUE.git

# 1. Acesse a pasta do projeto
$ cd Fashion-Avenue

# 2. Crie e ative o ambiente virtual (virtualenv)
$ python -m venv venv
$ source venv/bin/activate  # Linux e Mac
$ venv\Scripts\Activate  # Windows

# 3. Instale as dependências do projeto
$ pip install -r requirements.txt

# 4. Execute as migrações do banco de dados
$ python manage.py migrate

# 5. Crie um superusuário para acessar o admin do Django
$ python manage.py createsuperuser

# 6. Execute o servidor em modo de desenvolvimento
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://localhost:8000>
🎯 Aqui estão as principais rotas da API de e-commerce:

🔑 Autenticação de Usuários:

    POST /users/login/ Dar acesso ao usuário
    POST /users/logout/ Desconecta o usuário
    POST /users/registration/ Resgistra um usuário
```
<div align="center">
    <img src="assets/request-users-login.png" style="max-width: 100%; height: auto; width: 500px;"/>
    <img src="assets/request-users-logout.png" style="max-width: 100%; height: auto; width: 500px;"/>
    <img src="assets/request-users-registration.png" style="max-width: 100%; height: auto; width: 500px;"/>
</div>

```bash

🛒 Produtos:

    GET /products/ - Retorna a lista de produtos disponíveis.
    GET /categories/slug/{id}/products/slug/{id}/ - Retorna os detalhes de um produto específico.
    POST /categories/slug/{id}/products/slug/{id}/ - Cria um novo produto (requer autenticação de administrador).
    PUT /categories/slug/{id}/products/slug/{id}/ - Atualiza um produto (requer autenticação de administrador).
    DELETE /categories/slug/{id}/products/slug/{id}/ - Exclui um produto (requer autenticação de administrador).

    
📦 Categorias:

    GET /categories/ - Retorna a lista de categorias de produtos.
    GET /categories/slug/{id}/ - Retorna os detalhes de uma categoria específica.
    POST /categories/slug/{id}/ - Cria uma nova categoria (requer autenticação de administrador).
    PUT /categories/slug/{id}/ - Atualiza uma categoria (requer autenticação de administrador).
    DELETE /categories/slug/{id}/ - Exclui  uma categoria (requer autenticação de administrador).

🛍️ Carrinho de Compras:

    GET /cart-detail/ - Retorna os itens no carrinho de compras do usuário.
    POST /cart/ - Adiciona um produto ao carrinho.
    DELETE /cart/ - Remove um produto do carrinho.


🛠️ Tecnologias Utilizadas:
```
   ### Backend
- **Django**: [Documentação oficial do Django](https://docs.djangoproject.com/)
- **Django Rest Framework**: [Documentação oficial do Django Rest Framework](https://www.django-rest-framework.org/)

### Banco de Dados
- **PostgreSQL**: [Documentação oficial do PostgreSQL](https://www.postgresql.org/docs/)

### Bibliotecas
- **Pillow**: [Gerenciamento de imagens](https://pillow.readthedocs.io/)
- **dj_rest_auth**: [Autenticação de usuários com dj-rest-auth](https://dj-rest-auth.readthedocs.io/)
- **django-allauth**: [Autenticação de usuários com django-allauth](https://docs.allauth.org/)
- **django-filter**: [Criação de filtros com django-filter](https://django-filter.readthedocs.io/)