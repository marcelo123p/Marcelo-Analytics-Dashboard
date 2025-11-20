📊 Plataforma de Analytics para Restaurantes

Interface: https://github.com/user-attachments/assets/fce10549-c24c-43c3-a199-ba7d5aea1d11

Projeto desenvolvido como solução para o desafio God Level Coder — NOLA

🚀 Visão Geral

Esta aplicação foi criada para permitir que donos de restaurantes analisem suas vendas de maneira simples e rápida, funcionando como um mini “Power BI do Food Service”.

Ela integra:

Backend Node.js + Express

Banco PostgreSQL

Frontend JavaScript consumindo API via fetch()

Endpoint /vendas que retorna os dados estruturados do banco.

🏗️ Arquitetura Geral
Frontend (HTML + JS)
        |
     fetch()
        |
Backend Node.js/Express ----> PostgreSQL (Tabela: vendas)

🔹 Fluxo resumido

O usuário acessa a página.

A página chama a API usando fetch('/vendas').

O backend acessa o banco.

Os dados retornam em JSON.

O frontend exibe insights básicos (produto mais vendido, ticket médio etc).

📦 Backend (Node + Express)
✨ Endpoint principal
app.get('/vendas', async (req, res) => {
  const result = await pool.query('SELECT * FROM vendas');
  res.json(result.rows);
});


O endpoint consulta a tabela vendas usando pool.query()

Retorna um JSON com todas as vendas cadastradas.

Estrutura da tabela vendas
campo	tipo
id	serial
produto	text
quantidade	int
valor	numeric
data_venda	date
🌐 Frontend (HTML + JavaScript)
Exemplo simples do consumo da API
async function carregarVendas() {
  const resposta = await fetch('http://localhost:3000/vendas');
  const dados = await resposta.json();
  console.log(dados);
}
carregarVendas();


A partir desse JSON, a interface pode:

calcular o produto mais vendido

gerar gráficos básicos

listar vendas

exibir totais e métricas

🛠️ Tecnologias Utilizadas

Node.js + Express — Servidor e API

PostgreSQL + pgAdmin — Banco de dados

JavaScript — Lógica do frontend

Fetch API — Comunicação com o backend

VS Code (Linux Ubuntu) — Ambiente de desenvolvimento
