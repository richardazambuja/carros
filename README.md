# 🚗 CarStock – Sistema de Gerenciamento de Estoque de Veículos

O **CarStock** é um sistema web robusto e intuitivo, desenvolvido para atender às necessidades de concessionárias e lojas de veículos. Ele oferece uma solução abrangente para a gestão de inventário, controle de entrada/saída, métricas financeiras e um sistema de permissões baseado em hierarquia.



## 📌 Sobre o Projeto

Focado em organização, segurança e escalabilidade, o CarStock emprega uma arquitetura baseada em camadas e é otimizado para deploy em servidores **Linux**. Utiliza **Nginx** como servidor web e **uWSGI** como servidor de aplicação, garantindo alta performance e confiabilidade em ambiente de produção.

---

### Sessão "Lista de Carros":
<img width="1486" height="725" alt="Captura de tela de 2026-02-15 17-33-58" src="https://github.com/user-attachments/assets/c7ce2eaf-6372-4cd9-ad07-dde022d6105f" />



### Sessão "Cadastro de um Carro":

<img width="1457" height="1205" alt="Captura de tela de 2026-02-15 17-50-33" src="https://github.com/user-attachments/assets/ce933e57-f4f4-4826-b435-cd9a8904d818" />



### Sessão "Detalhes do Carro":

<img width="1463" height="1135" alt="Captura de tela de 2026-02-15 17-34-42" src="https://github.com/user-attachments/assets/14dec3be-4289-49b9-851b-47f85c1d4492" />



### Sessão "Edição de um Carro":

<img width="1457" height="1205" alt="Captura de tela de 2026-02-15 17-59-53" src="https://github.com/user-attachments/assets/56715151-38d1-4460-934b-d28dfea12117" />



### Sessão "Confirmação Deleção de um Carro":

<img width="1457" height="1205" alt="Captura de tela de 2026-02-15 17-45-32" src="https://github.com/user-attachments/assets/afcfb7e2-9233-48ac-bfee-6af0b7862b71" />



### Sessão "Criação de Conta":

<img width="1457" height="1205" alt="Captura de tela de 2026-02-15 18-04-30" src="https://github.com/user-attachments/assets/decf3b0d-a92d-4a17-9fd7-3db6379bf1cf" />



### Sessão "Login":

<img width="1457" height="1205" alt="Captura de tela de 2026-02-15 18-04-38" src="https://github.com/user-attachments/assets/f49fd694-5101-4b9e-90db-19a5c6c96315" />



## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia(s) |
| :--- | :--- |
| **Backend** | Python, Django |
| **Banco de Dados** | PostgreSQL (Produção), SQLite (Dev) |
| **Frontend** | HTML5, CSS3 (Django Templates) |
| **Servidor Web** | Nginx |
| **Application Server** | uWSGI |
| **Deploy** | VPS Linux (AWS EC2) |
| **Versionamento** | Git, GitHub |

---

## 🏗️ Arquitetura do Sistema

O projeto segue as melhores práticas de desenvolvimento com Django, promovendo modularidade e fácil manutenção:

* **Separação de Apps:** Aplicações independentes para facilitar a escalabilidade.
* **Padrão MVT:** Implementação do *Model-View-Template* para separação de responsabilidades.
* **Gestão de Media:** Configuração otimizada para upload e armazenamento de imagens de veículos em `/media/cars/`.
* **Hierarquia de Permissões:** Sistema de autenticação e autorização nativo do Django.



---

## 🔐 Hierarquia de Usuários

| Tipo de Usuário | Permissões |
| :--- | :--- |
| **👑 Administrador** | Cadastro, edição, exclusão, acesso total a métricas e relatórios financeiros. |
| **👤 Funcionário** | Cadastro e edição de veículos no estoque. |

---

## 🚘 Funcionalidades

### 📦 Gestão de Estoque
- **Cadastro Completo:** Registro de preço de compra, preço de venda e status (Disponível/Vendido).
- **Upload de Fotos:** Suporte a imagens reais do veículo com sistema de *fallback* (imagem padrão).
- **Fluxo de Entrada/Saída:** Controle rigoroso da movimentação do pátio.

### 📊 Métricas e Relatórios (Exclusivo Admin)
- **Inventário:** Visão geral da quantidade de carros em estoque.
- **Histórico de Vendas:** Acompanhamento mensal do desempenho comercial.
- **Volume Financeiro:** Monitoramento do valor total movimentado e giro de capital.

---

## 📈 Melhorias Futuras

- [ ] **Dashboard Interativo:** Gráficos dinâmicos com **Chart.js**.
- [ ] **API RESTful:** Integração externa via **Django Rest Framework**.
- [ ] **Exportação de Relatórios:** Geração de documentos em **PDF**.
- [ ] **Multi-Loja:** Gerenciamento de múltiplas filiais em uma única conta.
- [ ] **Comissões:** Módulo para cálculo automático de comissão por vendedor.
- [ ] **Auditoria (Logs):** Rastreabilidade total de alterações no sistema.

---

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/carstock.git](https://github.com/seu-usuario/carstock.git)
    ```
2.  **Crie um ambiente virtual e instale as dependências:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    pip install -r requirements.txt
    ```
3.  **Execute as migrações e inicie o servidor:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
