# ⚽ Flashscore Data Engine

Pipeline de engenharia de dados para coleta, processamento e estruturação de dados esportivos a partir do Flashscore, utilizando engenharia reversa e execução incremental.

## 🎯 Objetivo

Construir uma infraestrutura de dados esportivos escalável para alimentar modelos de Machine Learning e estratégias baseadas em valor esperado (EV+).

## 🚀 Funcionalidades

- Scraping histórico de ligas (2023+)
- Coleta de eventos, estatísticas e odds
- Pipeline incremental com controle de estado
- Deduplicação automática
- Estrutura modular e escalável

## 📁 Estrutura

config/   → configurações (ligas, run_config, bookmakers)  
scripts/  → etapas do pipeline  
utils/    → funções auxiliares  
output/   → dados coletados  
state/    → controle de progresso  
logs/     → logs de execução  

## ▶️ Como rodar

```bash
python scripts/run_passados.py
```

## ⚙️ Configuração

Editar:

```json
config/run_config.json
```

Exemplo:

```json
{
  "test_mode": false,
  "start_date": "2023-01-01",
  "end_date": "yesterday",
  "headless": true
}
```

## 🧠 Pipeline

1. Coleta de eventos por liga
2. Coleta de feeds das partidas
3. Coleta de odds
4. Parsing e normalização
5. Construção da base unificada

## ☁️ Execução Automatizada

O pipeline é executado automaticamente via GitHub Actions, sem necessidade de infraestrutura local.

Características:

* Execução periódica em ambiente cloud
* Processamento em lotes (batch) de ligas
* Controle de progresso via `state/`
* Continuidade automática entre execuções
* Persistência de estado e configuração

Fluxo:

```text
GitHub Actions → Executa pipeline → Atualiza state/config → Próximo ciclo continua
```

Agendamento atual:

```text
A cada 2 horas
```

O sistema foi projetado para rodar de forma incremental, evitando reprocessamento de dados e garantindo escalabilidade.

## 📌 Observações

- O pipeline é incremental (usa `state/`)
- Dados são armazenados em JSON
- Pode ser adaptado para SQL / Data Warehouse

## 🛠️ Tecnologias

- Python
- Playwright
- JSON / ETL
- GitHub Actions (CI/CD)
- Engenharia Reversa (Flashscore)

## 🔗 Integração

Este projeto alimenta o sistema:

- football_saas → Machine Learning + Backtest + Predições


## 👨‍💻 Autor

Vinicius Santos Medrado  
Analista de Dados & Automação
