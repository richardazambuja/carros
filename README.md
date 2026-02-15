🚗 CarStock – Sistema de Gerenciamento de Estoque de Veículos

Sistema web completo para gerenciamento de estoque de veículos, com controle de inventário, métricas financeiras e hierarquia de usuários.

📌 Sobre o Projeto

O CarStock é um sistema desenvolvido para concessionárias e lojas de veículos que precisam:

Controlar o estoque de carros

Gerenciar entrada e saída de veículos

Acompanhar histórico mensal

Visualizar métricas financeiras

Controlar permissões por hierarquia

O sistema foi desenvolvido com foco em organização, segurança e escalabilidade, utilizando arquitetura baseada em camadas e deploy em servidor Linux com Nginx e uWSGI.

Sessão 'Lista de Carros':
<img width="1486" height="725" alt="Captura de tela de 2026-02-15 17-33-58" src="https://github.com/user-attachments/assets/74eec2b7-0b87-45c6-b21a-6717419fb922" />

Sessão 'Detalhes do Carro':
<img width="1463" height="1135" alt="Captura de tela de 2026-02-15 17-34-42" src="https://github.com/user-attachments/assets/de4c5fc5-cc84-4888-8e6b-b3d5c3a1cbf2" />

Sessão 'Cadastrar um Carro'
<img width="1479" height="1128" alt="Captura de tela de 2026-02-15 17-34-22" src="https://github.com/user-attachments/assets/725dc175-f830-4fe9-993f-8f9b0cf2ff88" />

Sessão 'Editar um Carro':
<img width="1457" height="1205" alt="Captura de tela de 2026-02-15 17-34-55" src="https://github.com/user-attachments/assets/269bf51d-1989-4f51-adcf-eb6266b2f3ae" />

Sessão 'Confirmação de Deleção um Carro':
<img width="1457" height="1205" alt="Captura de tela de 2026-02-15 17-45-32" src="https://github.com/user-attachments/assets/45b8fbf8-e7d8-42ae-a956-2879f6a1fc4f" />


🛠️ Tecnologias Utilizadas

Backend: Python + Django

Banco de Dados: PostgreSQL / SQLite (ambiente de desenvolvimento)

Frontend: HTML, CSS (Django Templates)

Servidor: Nginx

Application Server: uWSGI

Deploy: VPS Linux (AWS EC2)

Versionamento: Git + GitHub

🏗️ Arquitetura do Sistema

O sistema foi estruturado seguindo boas práticas do Django:

Separação de apps

Uso de Models, Views e Templates

Configuração adequada de static e media

Upload de imagens com ImageField

Hierarquia de permissões baseada em autenticação Django

🔐 Hierarquia de Usuários
Tipo de Usuário	Permissões
Administrador	Cadastro, edição, exclusão, acesso a métricas e relatórios
Funcionário	Cadastro e edição de veículos
🚘 Funcionalidades
📦 Gestão de Estoque

Cadastro de veículos

Upload de foto

Preço de compra

Preço de venda

Status do veículo (Disponível / Vendido)

📊 Métricas e Relatórios (Admin)

Total de carros em estoque

Histórico mensal de vendas

Valor total já movimentado

Controle de giro financeiro

🖼️ Sistema de Imagens

Upload organizado em /media/cars/

Suporte a imagem padrão quando não há foto

📈 Melhorias Futuras

Dashboard com gráficos (Chart.js)

API REST com Django Rest Framework

Exportação de relatórios em PDF

Sistema multi-loja

Controle de comissão de vendedores

Auditoria de alterações
