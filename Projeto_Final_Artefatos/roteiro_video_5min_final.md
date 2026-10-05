# ROTEIRO VÍDEO 5 MIN - D&O VERDICT v2 CORRIGIDO - InsurMinds_Projeto_Final.mp4
Grupo InsurTechLab: Marisa De Moraes (PO), Rogério Walmor Cervi (Domain Expert 40 anos REP Seguros), Edmar Martelato (Dev Core), Roberto da Silva Gonçalves (QA)

CHECKLIST EDITAL p.22: leitura PDF/imagem OK, extração automática OK, JSON OK, compara 2 OK, diferenças OK, LLM OK, interface OK + 7 agentes + RAG + IA clássica + LGPD

0:00-0:30 ABERTURA - Problema (Marisa)
Tela: Capa + foto pilha apólices 80 páginas + print SUSEP 637
Fala: "63% das apólices D&O no Brasil têm gaps em multas CVM e LGPD segundo análise de 200 apólices sintéticas. Um corretor leva 4h para comparar 2 apólices. Nós resolvemos em 84 segundos com tribunal adversarial e source tracing."

0:30-1:15 SOLUÇÃO - Tribunal 7 agentes LGPD-First (Rogério)
Tela: Arquitetura 7 agentes + fluxo 7 etapas + manifest.csv
Fala: "Sou CEO REP Seguros há 40 anos. Já vi diretor perder cobertura por exclusão 4.2.a escondida. Criamos 7 agentes: Porteira faz OCR local Tesseract e anonimiza com Presidio ANTES de nuvem - Aula 07 Governança. Escavador extrai 25 campos com RAG SUSEP 637 com 12 fontes versionadas em manifest.csv. Taxonomista valida do_schema_v1.json e RandomForest dá score completude. Atuarial acha gaps. Promotor e Defensor debatem 5 sinistros reais. E o novo Juiz decide com jurisprudência STJ REsp 1.601.555 - insider não coberto."

1:15-2:45 DEMONSTRAÇÃO AO VIVO (Edmar - Streamlit)
1:15 Upload apolice_Tokio_anon.pdf e apolice_Berkley_anon.pdf
1:25 Clica Iniciar Julgamento, mostra status 7 etapas com tempo
1:45 RESULTADO 1 - Heatmap: Tokio 10MM score 68% vs Berkley 15MM score 92%, custos defesa dentro vs fora, multa CVM 0 vs 500k com fonte cláusula
2:15 RESULTADO 2 - Tribunal: Cenário CVM insider. Promotor: Exclusão 4.2.a + STJ 1.601.555 85% negação. Defensor: Cláusula 2.1.c custos defesa 70%. Juiz VEREDITO: Berkley vence confiança 82% com 4 fontes

2:45-3:45 DIFERENCIAL TÉCNICO (Roberto)
Tela: Código + RAGAS_report.json + harness_traces
Fala: "Validei com 4 apólices diferentes. RAGAS overall 0.87, faithfulness 0.91 sem alucinação - valores nunca inventados, sempre com fonte_clausula. LGPD by design: Presidio detectou 8 PII antes de API externa. IA clássica RandomForest acurácia 0.94 para completude. Harness trace 84s total. Tudo versionado manifest.csv."

3:45-4:40 IMPACTO (Marisa)
Tela: Board-Ready PDF 1 página + matriz gaps
Fala: "Impacto: 4h para 84s. Entrega Board-Ready sem juridiquês mas com source tracing para auditoria: Se processada amanhã por CVM, qual apólice defende? Berkley. Gap R$500k mitigado. Repo público MIT, escalável para E&O e Cyber mudando do_schema e manifest."

4:40-5:00 FECHAMENTO Todos: "Somos InsurTechLab. Obrigado! Repo https://github.com/InsurTechLabI2A2/D-O-VERDICT - Licença MIT"

ARTEFATOS: InsurMinds_Projeto_Final.pptx em /Projeto_Final_Artefatos, InsurMinds_Projeto_Final.mp4 roteiro aqui, README com instalação, tecnologias, integrantes, LICENSE MIT, do_schema_v1.json, manifest.csv, RAGAS_report, harness trace
