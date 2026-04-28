# ⚽ Flashscore Data Enginer

Pipeline completo de engenharia de dados para coleta, processamento e estruturação de dados esportivos (Flashscore).

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

1. Coleta de eventos
2. Coleta de feeds
3. Coleta de odds
4. Parse dos dados
5. Construção da base final

## 📌 Observações

- O pipeline é incremental (usa `state/`)
- Dados são armazenados em JSON
- Pode ser adaptado para SQL / Data Warehouse

## 👨‍💻 Autor

Vinicius Santos Medrado  
Analista de Dados & Automação
