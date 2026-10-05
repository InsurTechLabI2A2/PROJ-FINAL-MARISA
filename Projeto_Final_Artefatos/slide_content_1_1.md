# D&O VERDICT v2 - Tribunal Inteligente de Apólices - I2A2 InsurMinds

## Cover
# D&O VERDICT v2 - TRIBUNAL INTELIGENTE
### Não comparamos, JULGAMOS com source tracing STJ + SUSEP
Grupo InsurTechLab | Marisa, Rogério (40 anos REP), Edmar, Roberto | I2A2 Brasil Turma 1 2026
Imagem: foto profissional de pilha de apólices D&O + tribunal

---

## Problem
# O problema: 4h para comparar, gap R$500k escondido
- 63% das apólices D&O têm gaps em multas CVM/LGPD (base 200 apólices sintéticas + SUSEP 637)
- Corretor leva 4h lendo 80 páginas com exclusão 4.2.a escondida
- Diretores perdem cobertura por juridiquês - caso real REP Seguros
- Sem RAG com fonte, veredito vira alucinação
Visual: gráfico de tempo 4h vs 84s + heatmap de gaps

---

## Solution
# Solução: Tribunal Adversarial LGPD-First + Juiz STJ
- De 5 para 7 agentes corretos + 7 etapas LGPD-First
- Porteira: Tesseract local -> Presidio anonimiza ANTES de nuvem
- Escavador: RAG SUSEP 637 com 12 fontes versionadas em manifest.csv + PACE prompt
- Juiz novo: decide com STJ REsp 1.601.555 insider não coberto
- Board-Ready 1 página com source tracing auditável
Visual: arquitetura 7 agentes

---

## Architecture Corrected
# Arquitetura Corrigida v2 - 7 Agentes Mapeados
**01 Porteira** - Ingestão multimodal LGPD-First | Aula 07,20,22
**02 Escavador** - Extração semântica RAG SUSEP + Gemini + GPT-4o-mini | Aula 04,05
**03 Taxonomista** - Normalização do_schema_v1.json + RandomForest | Aula 12/13
**04 Atuarial** - Gap Analysis sublimites | Aula 02
**05 Promotor** - Ataca cobertura 85% negação | Aula 17
**06 Defensor** - Defende segurado Cláusula 2.1.c | Aula 17
**07 Juiz+Narrador** - Veredito + Heatmap + Board PDF + Harness | Aula 06,18,20
Orquestração: LangGraph + MCP + A2A
Visual: diagrama fluxo 7 etapas

---

## LGPD Fix
# Correção Crítica: LGPD by Design quebrado -> corrigido
**v1 errado:** PDF -> Azure Document Intelligence (nuvem) -> Presidio (tarde demais)
**v2 correto:** PDF -> Tesseract local -> Presidio detecta 8 PII -> Llama3 local anonimiza -> pronto_para_nuvem=True -> só então Azure/Gemini opcional
Aula 07 Governança + Aula 22 Privacidade atendida. Log em harness trace.
Visual: diagrama before/after LGPD

---

## RAG Governance
# RAG com Governança - manifest.csv versionado
- 12 fontes: SUSEP 637 principal, 621, 553, STJ REsp 1.601.555, LGPD art 52, 4 modelos anonimizados Tokio/Berkley/Fairfax/Pottencial, Nota Técnica SUSEP, ANPD
- Top-4 chunks com source tracing obrigatório no veredito
- Exemplo veredito: "Berkley vence - Base: Cláusula 2.3.b + SUSEP 637 art 3 + STJ 1.601.555"
- RAGAS overall 0.87, faithfulness 0.91 - sem alucinação, valores nunca inventados
Visual: tabela manifest.csv

---

## Classic AI
# IA Clássica - RandomForest Score Completude
- Dataset sintético 200 apólices rotuladas por Rogério domain expert 40 anos
- Features: limite_max, sublimite_CVM, sublimite_LGPD, tem_custos_fora_limite, tem_extensao_subsidiaria
- Modelo: RandomForest 100 árvores - Acurácia 0.94
- Features importance: sublimite_CVM 0.42 mais importante
- Explica por que Tokio 68% vs Berkley 92%
Aula 12/13 IA Clássica atendida - não é tudo LLM
Visual: gráfico feature importance + acurácia

---

## Tribunal Adversarial
# Tribunal Adversarial com Juiz - Diferencial
**Cenário 1 CVM Insider Trading**
Promotor: Exclusão 4.2.a ato doloso + STJ REsp 1.601.555 unanimidade 3a Turma - Prob negação 85%
Defensor: Cobertura A protege patrimônio pessoal, custos defesa desde notificação Cláusula 2.1.c - Prob cobertura 70%
Juiz: Berkley vence - cobre multa CVM R$500k vs Tokio exclui. Fontes: Cláusula 2.3.b Berkley + SUSEP 637 art 3 + STJ + SUSEP Nota Técnica. Confiança 82%
Outros 4 cenários: LGPD R$2MM, Trabalhista EPL, RJ insolvência, Greenwashing E&O
Visual: debate Promotor x Defensor x Juiz

---

## Demo
# Demo Ao Vivo - 84 segundos - Do PDF ao Veredito
1 Upload apolice_Tokio_anon.pdf + apolice_Berkley_anon.pdf
2 Status 7 etapas: Porteira 12s PII 8, Escavador 18s RAG 4 chunks confiança 0.92, Taxonomista score 68 vs 92, Atuarial 3 gaps, Promotor, Defensor, Juiz veredito
3 Heatmap: Tokio 10MM vermelho CVM, Berkley 15MM verde CVM 500k, custos fora limite verde
4 Tribunal: CVM insider - veredito Berkley com 4 fontes
Visual: screenshot Streamlit app + Harness trace timeline

---

## Evaluation
# Avaliação - RAGAS + Harness + 4 Apólices
- RAGAS_report.json: faithfulness 0.91, answer_relevancy 0.89, context_precision 0.87, context_recall 0.85, overall 0.87
- Harness trace sample_trace.json: 84s total, cada agente logado, pronto para LangSmith
- Teste Roberto: 4+ apólices diferentes - Tokio, Berkley, Fairfax, Pottencial - sem alucinação
- Anti-alucinação: valores nunca inventados, sempre fonte_clausula
Aula 20 avaliação + Aula 18 observabilidade atendidas
Visual: gráfico RAGAS + timeline Harness

---

## Impact
# Impacto Board-Ready - De juridiquês para decisão
**Pergunta Board:** Se processada amanhã por CVM, qual apólice defende melhor?
**Resposta:** Berkley R$15MM
- Gap crítico: Tokio não cobre multa CVM R$500k em risco
- Custos defesa: Berkley fora do limite - preserva limite para indenização
- Score completude: Tokio 68% vs Berkley 92% (RandomForest)
- Recomendação: contratar Berkley + extensão nova subsidiária + prazo suplementar 12 meses
Entrega: PDF 1 página + JSON estruturado + heatmap
Tempo: 4h -> 84s (95% redução SLA)
Escalável: E&O, Cyber mudando do_schema e manifest
Visual: Board-Ready PDF mock

---

## Team
# Time InsurTechLab - Divisão Clara
**Marisa De Moraes - PO** - Gestão projetos IA Aula 01, arquitetura, sprints, board-ready, governança LGPD
**Rogério Walmor Cervi - Domain Expert 40 anos CEO REP Seguros** - 2 modelos reais Tokio/Berkley, valida do_schema_v1.json (coberturas A/B/C, exclusões críticas), define 5 cenários tribunal, valida linguagem board
**Edmar Martelato - Dev Core** - agents 01-07, orchestrator LangGraph, app/streamlit_app.py, populate_chroma_susep.py, requirements.txt
**Roberto da Silva Gonçalves - Validador QA** - Teste 4+ apólices, RAGAS >0.87, valida score completude IA clássica, anti-alucinação, checklist p.22
Visual: fotos time

---

## Closing
# Obrigado - D&O VERDICT v2 Corrigido
Repo corrigido: https://github.com/InsurTechLabI2A2/D-O-VERDICT - Licença MIT real
Instalação: git clone + pip install + streamlit run app/streamlit_app.py
Artefatos: do_schema_v1.json v1.0.0 SUSEP 637, manifest.csv 12 fontes, RAGAS_report.json 0.87, harness trace 84s, roteiro_video_5min_final.md
Próximos passos: escalar para E&O, Cyber, D&O global com jurisprudência US/UK
Somos InsurTechLab - Não comparamos, JULGAMOS com fonte
Visual: QR code repo + logo I2A2

---
