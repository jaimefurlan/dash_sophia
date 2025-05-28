# 📘 ESPECIFICAÇÃO – FASE 1 DO DASHBOARD DA SOPHIA

## 🎯 OBJETIVO
Construir um dashboard web interativo e gratuito, capaz de exibir indicadores de performance da IA SophIA e dados de negócio em tempo real e históricos, com filtros por **data**, **hora** e **campanha**.

---

## 1. 🌐 ARQUITETURA

### 🔸 Visão Geral

```
+-------------+           +------------------+           +-------------------+
| Endpoints   |  --->     | Coletor de Dados |  --->     | Banco de Dados    |
| (JSON APIs) |           | (Python Script)  |           | Supabase (Postgre)|
+-------------+           +------------------+           +-------------------+
                                                              ↓
                                                       +--------------+
                                                       | Streamlit UI |
                                                       +--------------+
                                                             ↓
                                                    Streamlit Cloud (Free)
```

---

## 2. 🧰 STACK DE TECNOLOGIA

| Componente     | Tecnologia          | Observações                                                                 |
|----------------|---------------------|------------------------------------------------------------------------------|
| Frontend       | Streamlit           | Rápido, simples, Python puro, interativo                                     |
| Backend opcional | FastAPI (futuro)   | Caso queira padronizar os endpoints antes de chegar ao banco                |
| Coleta de Dados| Python agendado ou n8n | Para consumir os endpoints e popular o banco                                |
| Banco de Dados | Supabase            | PostgreSQL, gratuito até 500MB, suporta REST e consultas complexas          |
| Hospedagem     | Streamlit Cloud     | Grátis, fácil de conectar com GitHub                                        |

---

## 3. 📁 ESTRUTURA DE DADOS (TABELA)

```sql
CREATE TABLE sophia_dashboard (
  id SERIAL PRIMARY KEY,
  data DATE,
  hora INT,
  campanha TEXT,
  precisao FLOAT,
  velocidade_processamento FLOAT,
  taxa_erro FLOAT,
  latencia FLOAT,
  tokens INT,
  custo_tokens FLOAT,
  sessoes_chat INT,
  status_finalizacao TEXT,
  duracao_sessao FLOAT,
  consultas_por_sessao INT,
  comprimento_consulta INT,
  nps INT
);
```

---

## 4. 📊 INDICADORES E FILTROS

### 🧩 Filtros:
- `data` (intervalo)
- `hora` (por hora)
- `campanha` (filtro por nome)

### 📈 Indicadores IA:
- Precisão e Confiabilidade
- Velocidade de Processamento
- Taxa de Erros
- Latência
- Quantidade de Tokens Utilizados
- Custo de Tokens

### 📈 Indicadores de Negócio:
- Quantidade de Sessões de Chat
- Sessões por Status de Finalização
- Duração Média das Sessões
- Consultas por Sessão
- Comprimento da Consulta
- Taxa de Abandono
- NPS / Satisfação do usuário

---

## 5. ✅ PLANO DE EXECUÇÃO – FASE 1

### 🟩 ETAPA 1 – Preparação de ambiente
- [ ] Criar repositório no GitHub
- [ ] Conectar com Streamlit Cloud
- [ ] Criar ambiente Supabase com tabela `sophia_dashboard`

### 🟨 ETAPA 2 – Mock de dados
- [x] Gerar dataset com 500 registros aleatórios
- [ ] Subir para o Supabase (pode ser via CSV, insert ou script Python)
- [ ] Validar acesso remoto (via `supabase-py`)

### 🟦 ETAPA 3 – Streamlit Frontend
- [ ] Criar `app.py` com layout base:
  - Seções: filtros, indicadores IA, indicadores negócio
  - Tela "Hello, este é o dashboard da SophIA"
- [ ] Criar `requirements.txt`
- [ ] Testar localmente

### 🟥 ETAPA 4 – Deploy
- [ ] Subir código no GitHub
- [ ] Conectar repositório ao Streamlit Cloud
- [ ] Publicar projeto online com acesso público

---

## 6. 📎 ENTREGA FINAL DESTA FASE

- Repositório GitHub com:
  - `app.py`
  - `requirements.txt`
  - `.streamlit/config.toml` (opcional para layout customizado)
- Projeto online no Streamlit Cloud com:
  - Tela inicial (hello world + estrutura de layout)
  - Filtros funcionais (mesmo que ainda sem dados reais)