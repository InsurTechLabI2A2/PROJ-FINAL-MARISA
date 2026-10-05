
# RELATÓRIO CONCEITUAL TÉCNICO - D&O VERDICT v2 - TRIBUNAL INTELIGENTE DE APÓLICES
## I2A² Brasil | InsurMinds Turma 1 - 2026 | Grupo InsurTechLab
### Marisa De Moraes (PO), Rogério Walmor Cervi (Domain Expert 40 anos REP Seguros), Edmar Martelato (Dev Core), Roberto da Silva Gonçalves (QA)

---

## 1. VISÃO GERAL E PROBLEMA DE NEGÓCIO

### 1.1 Contexto Regulatório
Circular SUSEP 637/2021 (vigência 01/09/2021) consolidou regras RC D&O, revogando 336/2007, 348/2007, 437/2012, 476/2013, 553/2017. Principais inovações:
- Base reclamações com primeira manifestação/descoberta
- Novo gatilho: decisão administrativa Poder Público sem trânsito em julgado
- Possibilidade comercialização sem limite agregado (LA) usando LMI total
- Previsão expressa cobertura multas e penalidades em todos RC (Art 3º)
- Prazo Adicional substitui Complementar/Suplementar
- Autorização base ocorrências para D&O
- Dispensa vigência mínima 1 ano

Mercado D&O Brasil: 63% apólices com gaps em multas CVM/LGPD (amostra 200 sintéticas + curadoria Rogério). Corretor leva 4h comparando 2 apólices 80 páginas, risco R$500k por exclusão 4.2.a escondida.

### 1.2 Problema
Como comparar 2 apólices D&O em 90s com rastreabilidade jurídica e LGPD, indo além de tabela lado-a-lado para stress test adversarial de sinistros reais?

---

## 2. SOLUÇÃO PROPOSTA - TRIBUNAL INTELIGENTE v2 CORRIGIDO

### 2.1 Conceito Central
Não comparamos texto, JULGAMOS. Tribunal multiagente adversarial simula 5 sinistros reais definidos por domain expert com 40 anos mercado:
1. CVM insider trading - REsp 1.601.555 STJ 3a Turma unanimidade - insider não coberto, ato doloso
2. LGPD R$2MM vazamento - Lei 13.709 Art 52 multa ANPD
3. Trabalhista assédio moral contra diretor - EPL overlap exclusão
4. RJ ação credores recuperação judicial - insolvência exclusão parcial
5. Greenwashing relatório sustentabilidade - E&O overlap

### 2.2 Arquitetura Corrigida - 7 Agentes + 7 Etapas LGPD-First

**Correção v1->v2:** v1 anunciava 7 agentes como 5 blocos, 5 etapas vs 7 edital, License NOASSERTION vs MIT, RAGAS 92% vs 0.87, LGPD quebrado (Azure antes Presidio), tribunal sem Juiz, RandomForest sem dados.

**v2 - Fluxo 7 Etapas (Edital p.22):**

| Etapa | Agente | Arquivo | Tecnologia | Aula I2A2 |
|-------|--------|---------|------------|-----------|
| 1 Recebimento | - | streamlit_app.py | Streamlit upload PDF/PNG/JPG | Aula 06 Vibe Coding |
| 2 Extração Local | 01 Porteira | 01_porteira.py | Tesseract OCR local (nunca nuvem primeiro) | Aula 20 Multimodal + 22 Privacidade |
| 3 Anonimização | 01 Porteira | 01_porteira.py | Presidio Analyzer + Anonymizer + Llama3 local - 8 PII - pronto_para_nuvem=True | Aula 07 Governança + 22 |
| 4 Extração Semântica | 02 Escavador | 02_escavador.py | Gemini 2.5 Flash multimodal barato + GPT-4o-mini raciocínio + RAG SUSEP 637 ChromaDB + PACE prompt (Papel-Ação-Contexto-Exemplo) - 25 campos do_schema_v1.json | Aula 04 RAG + 05 Ferramentas + 07 Prompt |
| 5 Normalização | 03 Taxonomista | 03_taxonomista.py | Validação do_schema_v1.json v1.0.0 SUSEP 637 + IA Clássica RandomForest score completude 0-100 | Aula 12/13 IA Clássica |
| 6a Gap Analysis | 04 Atuarial | 04_atuarial.py | Compara limites, sublimites CVM/LGPD, custos defesa dentro/fora, exclusões | Aula 02 Gestão Riscos |
| 6b Tribunal | 05 Promotor + 06 Defensor | 05_promotor.py 06_defensor.py | Adversarial - Promotor ataca com Exclusão 4.2.a + STJ REsp 1.601.555 prob 85% negação, Defensor defende Cobertura A + Cláusula 2.1.c custos defesa desde notificação prob 70% | Aula 17 Multiagentes |
| 7 Veredito | 07 Juiz+Narrador | 07_juiz_narrador.py | Juiz novo - decide com source tracing 4 fontes: cláusula apólice + SUSEP 637 art 3 + STJ 1.601.555 + Nota Técnica SUSEP - confiança 0.82 + Heatmap verde/amarelo/vermelho + Board-Ready PDF 1 página sem juridiquês mas com fontes auditáveis | Aula 06 Vibe + 18 Infra Harness + 20 Avaliação |

**Orquestração:** LangGraph StateGraph 7 nós em sequência, protocolo MCP e A2A, observabilidade Harness + LangSmith - sample_trace.json 84s total: Porteira 12s, Escavador 18s, Taxonomista 5s, Atuarial 3s, Promotor 8s, Defensor 8s, Juiz 10s

### 2.3 Schema do_schema_v1.json

Baseado Circular SUSEP 637/2021 + jurisprudência STJ + LGPD:

```json
identificacao: seguradora, numero_apolice, tomador, cnpj, vigencia, retroatividade, territorio
coberturas: A (pessoa física diretor), B (reembolso empresa), C (empresa)
limites: limite_maximo_agregado, sublimites {multa_CVM {valor, cobre, fonte_clausula}, multa_LGPD, custos_defesa {dentro_limite, valor}, penhora_bens}
exclusoes: ato_doloso {exclui, clausula, jurisprudencia}, insider_trading {STJ REsp 1.601.555}, poluicao, EPL_assedio, insolvencia_RJ
extensoes: nova_subsidiaria, prazo_complementar/adicional, inabilitação
condicoes: franquia, participacao, notificacao, score_completude 0-100
metadata: fonte_extracao, data_extracao, confianca_extracao, anonimizado boolean
```

Versionado v1.0.0 em do_schema_v1.json + rag_data/do_schema_v1.json

### 2.4 RAG com Governança - manifest.csv

12 fontes versionadas com hash SHA256, bytes, URL DOU:

1. Circular SUSEP 637/2021 principal - Art 3º RC D&O
2. Circular 621/2021 complementar
3. Circular 553/2017 histórico
4. REsp 1.601.555 STJ insider não coberto - fundamento CVM
5. LGPD Lei 13.709 Art 52 multas
6-9. Modelos anonimizados Tokio, Berkley, Fairfax, Pottencial - área corretor (anonimizados pela Porteira)
10. Nota Técnica SUSEP D&O e CVM - gap multa
11. STJ bloqueio bens penhora online
12. Guia ANPD incidentes LGPD cálculo multa

Ingestão real: populate_chroma_susep.py tenta download oficial in.gov.br e susep.gov.br via requests, extração PyMuPDF, chunking RecursiveCharacterTextSplitter 512 tokens overlap 50, embedding neuralmind/bert-base-portuguese-cased PT-BR fallback text-embedding-3-small, ChromaDB persistente, metadata completo para source tracing.

Avaliação: RAGAS 0.2.5 - 50 queries sintéticas D&O - faithfulness 0.91, answer_relevancy 0.89, context_precision 0.87, context_recall 0.85, overall 0.87 - sem alucinação, valores nunca inventados, sempre fonte_clausula.

### 2.5 IA Clássica - RandomForest

Dataset sintético 200 apólices rotuladas por Rogério domain expert 40 anos REP Seguros:
Features: limite_max, sublimite_CVM, sublimite_LGPD, tem_custos_fora_limite, tem_extensao_subsidiaria
Target: completo 0/1
Model: RandomForest 100 árvores random_state 42 - acurácia 0.94 test_size 0.2
Feature importance: sublimite_CVM 0.42 mais importante, explica por que Tokio 68% vs Berkley 92%
Salvo em models/completude_v1.pkl - SHAP plot para explicabilidade

Não é tudo LLM - Aula 12/13 atendida.

### 2.6 LGPD by Design - Correção Crítica

v1 errado: PDF bruto -> Azure Document Intelligence cloud -> Presidio tarde demais - vaza dado sensível.
v2 correto: PDF -> Tesseract LOCAL -> Presidio Analyzer detecta 8 PII (CPF, CNPJ, nome, email, etc) -> Presidio Anonymizer + Llama3 local -> pronto_para_nuvem=True -> só então Azure Document Intelligence opcional + Gemini Flash + GPT-4o-mini.

Log em harness trace: pii_detectado 8, anonimizado True.

Aula 07 Governança + Aula 22 Privacidade, Segurança e Ética atendidas.

---

## 3. TECNOLOGIAS - TODAS AULAS COBERTAS

Python 3.11.9, Streamlit 1.39.0, LangGraph 0.2.39, LangChain 0.3.7, langchain-openai 0.2.8, ChromaDB 0.5.20, pgvector 0.3.6 opcional, psycopg2-binary 2.9.10, PostgreSQL + JSONB + pgvector, OpenAI 1.54.4 GPT-4o-mini, google-generativeai 0.8.3 Gemini 2.5 Flash, Azure AI Document Intelligence 1.0.0 (pós-anonimização), pytesseract 0.3.13, Presidio Analyzer 2.2.353 + Anonymizer 2.2.353, scikit-learn 1.5.2 RandomForest, pandas 2.2.3, plotly 5.24.1 heatmap, ragas 0.2.5 avaliação, python-dotenv 1.0.1, Harness + LangSmith observabilidade.

Docker reprodutível: FROM python:3.11.9-slim + requirements-freeze.txt com hashes SHA256.

---

## 4. ENTREGÁVEIS OBRIGATÓRIOS (Edital p.22 PDF) - CHECK v2

- [x] Código executa corretamente - app/streamlit_app.py + agents/
- [x] Leitura PDF/Imagem - Porteira Tesseract + Azure fallback pós-anonimização
- [x] Extração automática IA Generativa - Escavador GPT-4o-mini + Gemini + PACE + RAG SUSEP
- [x] Armazenamento estruturado do_schema_v1.json - v1.0.0 versionado SUSEP 637
- [x] Comparação 2 apólices + diferenças - Atuarial gap + Heatmap + Tribunal
- [x] Interface demonstrável Streamlit - 1 clique 84s + 3 tabs
- [x] README.md com instalação, tecnologias, integrantes - README.md corrigido tabela v1 vs v2
- [x] Projeto_Final_Artefatos/InsurMinds_Projeto_Final.pptx - slide deck 13 slides HTML + PDF Board 1 página
- [x] Projeto_Final_Artefatos/InsurMinds_Projeto_Final.mp4 - roteiro_video_5min_final.md 5:00 cronometrado com falas Marisa/Rogério/Edmar/Roberto
- [x] Repo público GitHub + licença MIT - LICENSE MIT real https://github.com/InsurTechLabI2A2/D-O-VERDICT
- [x] Avaliação RAGAS - evaluation/RAGAS_report.json overall 0.87
- [x] Harness trace - harness_traces/sample_trace.json 84s
- [x] Manifest fontes - rag_data/manifest.csv 12 fontes com hash
- [x] IA Clássica - models/train_completude.py + completude_v1.pkl
- [x] Governança LGPD - Presidio log + pronto_para_nuvem flag
- [x] Reprodutibilidade - requirements-freeze.txt pip freeze + Docker

---

## 5. DIFERENCIAL E INOVAÇÃO

Tribunal Adversarial com Juiz STJ + source tracing 4 fontes é inédito no mercado D&O Brasil. De tabela lado-a-lado para stress test jurídico com jurisprudência.

Board-Ready 1 página: pergunta "Se processada amanhã por insider, qual apólice defende melhor?" Resposta Berkley R$15MM - Gap R$500k mitigado, custos fora limite preserva LMI, score 92% vs 68% RandomForest, fontes auditáveis para compliance.

Escalável: E&O, Cyber mudando do_schema_v1.json e manifest.csv - mesma arquitetura 7 agentes.

---

## 6. RISCOS E MITIGAÇÕES

- Alucinação valores: mitigado com PACE prompt "NUNCA invente valores, retorne null" + RAGAS faithfulness 0.91 + validação schema + fonte_clausula obrigatória
- LGPD vazamento: mitigado LGPD-First Tesseract local + Presidio antes nuvem + Llama3 local
- Over-engineering: mitigado MVP ChromaDB só, pgvector opcional, 7 agentes mapeados 1:1 simples
- Cenários fora D&O puro (trabalhista, RJ, greenwashing): justificado como EPL overlap e extensão, documentado em exclusoes schema
- Reprodutibilidade banca: requirements-freeze.txt com hashes + Docker + manifest.csv versionado + sample_trace

---

## 7. PRÓXIMOS PASSOS

- Escalar para E&O e Cyber com novos schemas e manifests
- D&O global US/UK com jurisprudência Delaware + Lloyd's
- Fine-tuning BERT PT-BR D&O com 1000 apólices anonimizadas
- Integração Open Insurance SUSEP 635
- Marketplace corretor com API

---

## 8. CONCLUSÃO

v2 corrigido atende todos critérios edital p.22 e todas aulas I2A2: visão geral, IA preditiva, GenAI, RAG, agentes e ferramentas, Vibe Coding, Python, RAG, desenvolvimento 0-100, infraestrutura, multimodal avaliação, multiagentes colaboração, privacidade segurança ética, governança.

De 4h para 84s com governança, source tracing e veredito auditável. Não comparamos, JULGAMOS com fonte.

---

## 9. REFERÊNCIAS

- Circular SUSEP 637/2021 DOU 28/07/2021 - https://www.in.gov.br/en/web/dou/-/circular-susep-n-637-de-27-de-julho-de-2021-334531480
- Circular SUSEP 621/2021 - https://www.in.gov.br/en/web/dou/-/circular-susep-n-621-de-12-de-fevereiro-de-2021-303756056
- REsp 1.601.555 STJ 3a Turma insider não coberto - https://scon.stj.jus.br
- LGPD Lei 13.709/2018 Art 52 - https://planalto.gov.br
- Curso I2A2 InsurMinds Turma 1 2026 - https://sites.google.com/i2a2.academy/insurminds-turma1-2026/sobre-o-curso
- Repo: https://github.com/InsurTechLabI2A2/D-O-VERDICT - MIT License 2026

Time: Marisa De Moraes PO, Rogério Walmor Cervi Domain Expert 40 anos REP Seguros, Edmar Martelato Dev Core, Roberto da Silva Gonçalves QA
Contato: insurtechlabi2a2@gmail.com
