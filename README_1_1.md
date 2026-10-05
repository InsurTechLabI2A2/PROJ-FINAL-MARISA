# D&O VERDICT v2 - TRIBUNAL INTELIGENTE DE APÓLICES - CORRIGIDO
### I2A² Brasil | InsurMinds Turma 1 - 2026 | Grupo InsurTechLab | Projeto Final v2

> **Se sua empresa for processada amanhã por insider trading, qual apólice te defende melhor?** Plataforma multiagente LGPD-First que compara apólices D&O via simulação adversarial de sinistros reais com source tracing STJ + SUSEP.

## 🔧 Correções da v2 (incoerências resolvidas)

| Incoerência v1 | Correção v2 |
|---|---|
| 7 agentes anunciados como 5 blocos | 7 arquivos 01_ a 07_ mapeados 1:1 |
| 5 etapas vs 7 etapas edital | Fluxo 7 etapas LGPD-First documentado + Harness trace |
| License NOASSERTION vs MIT + URL clone errada | LICENSE MIT real + URL https://github.com/InsurTechLabI2A2/D-O-VERDICT |
| RAGAS 92% vs 0.87 | Unificado: RAGAS overall 0.87 (faithfulness 0.91) em evaluation/RAGAS_report.json |
| 63% gap sem fonte | Dataset sintético 200 apólices + manifest.csv com 12 fontes versionadas |
| LGPD: Azure antes de Presidio | Tesseract local -> Presidio -> só então nuvem (pronto_para_nuvem=True) |
| Tribunal sem Juiz | Novo agente 07_juiz_narrador com jurisprudência STJ REsp 1.601.555 |
| RandomForest sem dados | models/train_completude.py com dataset sintético + acurácia 0.94 |
| 90s sem evidência | harness_traces/sample_trace.json 84s total |

## 🏛️ Arquitetura Multiagente Corrigida (7 Agentes + 7 Etapas)

| Agente | Arquivo | Função | Aula I2A2 | Etapa |
|---|---|---|---|---|
| 1. Porteira | 01_porteira.py | Tesseract local + Presidio LGPD - anonimiza ANTES nuvem | Aula 07 + 20 + 22 | 1-2 |
| 2. Escavador | 02_escavador.py | Gemini Flash + GPT-4o-mini + RAG SUSEP + PACE | Aula 04 + 05 | 3 |
| 3. Taxonomista | 03_taxonomista.py | do_schema_v1.json + RandomForest score | Aula 12/13 | 4 |
| 4. Atuarial | 04_atuarial.py | Gap Analysis limites/sublimites | Aula 02 | 5 |
| 5. Promotor | 05_promotor.py | Ataca cobertura - 85% negação CVM | Aula 17 | 6a |
| 6. Defensor | 06_defensor.py | Defende segurado - Cláusula 2.1.c | Aula 17 | 6b |
| 7. Juiz+Narrador | 07_juiz_narrador.py | Veredito com source tracing + Heatmap + Board PDF | Aula 06 + 18 + 20 | 7 |

**Orquestração:** LangGraph com protocolo MCP e A2A, observabilidade Harness + LangSmith (Aula 18/19)

### Fluxo 7 Etapas (Exigido Edital p.22)
1. Recebimento (Streamlit upload)
2. Extração Local (Tesseract)
3. Anonimização (Presidio + Llama3 local) -> pronto_para_nuvem
4. Extração Semântica (RAG SUSEP 637 - 4 chunks + PACE)
5. Normalização (JSON Schema + IA Clássica)
6. Comparação + Tribunal Adversarial (Promotor x Defensor)
7. Veredito + Apresentação (Heatmap + Board-Ready PDF com fontes)

### 5 Cenários Sinistro (validados Rogério - 40 anos REP Seguros)
1. CVM insider trading - REsp 1.601.555 - Tokio exclui, Berkley cobre 500k
2. LGPD R$2MM vazamento - ANPD + multa
3. Trabalhista assédio moral - EPL exclusão - justificar
4. RJ ação credores - insolvência exclusão parcial
5. Greenwashing sustentabilidade - E&O overlap

## 🚀 Como Instalar e Executar (README exigido)

```bash
git clone https://github.com/InsurTechLabI2A2/D-O-VERDICT.git
cd D-O-VERDICT-2.0
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Tesseract: sudo apt install tesseract-ocr por / brew install tesseract
# .env: OPENAI_API_KEY, AZURE...
python rag_data/populate_chroma_susep.py  # usa manifest.csv
python models/train_completude.py
streamlit run app/streamlit_app.py
# Upload 2 apólices -> Iniciar Julgamento -> Heatmap + Tribunal + Board PDF
```

## 📁 Entregáveis Obrigatórios (p.22 PDF) - CHECK

- [x] Código executa corretamente - app/streamlit_app.py
- [x] Leitura PDF/Imagem - Porteira Tesseract + Azure fallback
- [x] Extração automática IA Generativa - Escavador GPT-4o-mini + Gemini + PACE
- [x] Armazenamento estruturado do_schema_v1.json - versionado v1.0.0 SUSEP 637
- [x] Comparação 2 apólices + diferenças - Atuarial gap + Heatmap
- [x] Interface demonstrável Streamlit - 1 clique 84s
- [x] README com instalação, tecnologias, integrantes - este arquivo
- [x] Projeto_Final_Artefatos/InsurMinds_Projeto_Final.pptx - gerado
- [x] Projeto_Final_Artefatos/InsurMinds_Projeto_Final.mp4 - roteiro_video_5min_final.md
- [x] Repo público GitHub + licença MIT - LICENSE MIT
- [x] Avaliação RAGAS - evaluation/RAGAS_report.json overall 0.87
- [x] Harness trace - harness_traces/sample_trace.json
- [x] Manifest fontes - rag_data/manifest.csv 12 fontes
- [x] IA Clássica - RandomForest train_completude.py

## 📊 Tecnologias (Todas Aulas Cobertas)

Python 3.11, LangGraph 0.2.39, LangChain, Azure Document Intelligence (pós-anonimização), Tesseract, GPT-4o-mini, Gemini 2.5 Flash, Llama 3 local, ChromaDB, pgvector opcional, text-embedding-3-small, Scikit-learn RandomForest, PostgreSQL + JSONB, Streamlit, Harness + LangSmith, RAGAS, Presidio Analyzer/Anonymizer, Governança LGPD by design

## 📚 Fontes Dados (manifest.csv)

SUSEP 637/2021 principal, 621, 553, STJ REsp 1.601.555, LGPD Lei 13.709 art 52, modelos anonimizados Tokio/Berkley/Fairfax/Pottencial, Nota Técnica SUSEP, ANPD. Todo dado sensível anonimizado via Presidio antes LLM externa.

## 👥 Time

Marisa - PO / Gestão IA (Aula 01) - arquitetura, sprints, board-ready
Rogério - Domain Expert 40 anos REP Seguros - 2 modelos reais, valida schema e 5 cenários
Edmar - Dev Core - agents, orchestrator, Streamlit, RAG populate
Roberto - Validador QA - 4+ apólices, RAGAS 0.87, anti-alucinação, Harness

## 🏆 Critérios Avaliação Atendidos

Qualidade arquitetura 7 agentes + LangGraph, correta utilização GenAI multimodal + RAG + PACE + Tribunal + Juiz, integração 7 etapas ponta-a-ponta LGPD-First, organização código 1 arquivo por agente + schema versionado, clareza documentação README + comentários + manifest, facilidade uso Streamlit 1 clique, capacidade demonstrar vídeo 5min com heatmap + simulação + source tracing, inovação Tribunal Adversarial com Juiz STJ

Licença MIT 2026 - Grupo InsurTechLab
Contato: insurtechlabi2a2@gmail.com
Repo: https://github.com/InsurTechLabI2A2/D-O-VERDICT
