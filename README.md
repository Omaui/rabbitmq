# Projeto RabbitMQ - Exemplo Básico com Producer, Consumer e Docker

Este projeto demonstra uma configuração simples do RabbitMQ usando Docker, além de exemplos básicos em Python (consumer) e Node.js (producer) para enviar e receber mensagens em uma fila.

---

## O que é RabbitMQ?

RabbitMQ é um message broker que permite a comunicação assíncrona entre aplicações por meio de filas de mensagens.

---

## 🚀 Como executar o projeto

### 1. Subir o RabbitMQ via Docker

Use o docker-compose para iniciar o RabbitMQ com interface de gerenciamento:

Para isso, execute o comando: `docker-compose up -d`

A interface web estará disponível em: http://localhost:15672  
Usuário: `guest`  
Senha: `guest`

---

### 2. Executar o consumidor (consumer) em Python

O consumidor fica ouvindo a fila `messages` e imprime as mensagens recebidas.

Execute no terminal: `python consumer.py`

---

### 3. Executar o produtor (producer) em Node.js

O produtor envia a mensagem "Hello Queue" para a fila `messages`.

Execute no terminal: `node producer.js`

---

## 🗂 Estrutura do projeto

- consumer.py         — Código do consumidor em Python  
- producer.js         — Código do produtor em Node.js  
- docker-compose.yml  — Configuração do RabbitMQ via Docker

---

## 📋 Descrição dos arquivos

- **consumer.py**: conecta ao RabbitMQ, escuta a fila `messages` e imprime as mensagens recebidas.  
- **producer.js**: conecta ao RabbitMQ, envia uma mensagem "Hello Queue" para a fila `messages`.  
- **docker-compose.yml**: sobe um container RabbitMQ com interface web de gerenciamento.

---

## 📚 Tecnologias utilizadas

- RabbitMQ (via Docker)  
- Python (pika) para consumidor  
- Node.js (amqplib) para produtor  
- Docker e Docker Compose

---
