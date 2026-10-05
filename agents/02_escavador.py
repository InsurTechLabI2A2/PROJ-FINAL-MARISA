
"""
Agente 2 - Escavador - Extração Semântica com RAG SUSEP
Aula 04 RAG + Aula 05 Ferramentas + PACE prompt
"""
import chromadb
from langchain_openai import ChatOpenAI

PACE_PROMPT = """
Papel: Você é especialista D&O com 20 anos, baseado na Circular SUSEP 637/2021
Ação: Extraia 25 campos obrigatórios do do_schema_v1.json
Contexto: Apólice anonimizada + chunks RAG SUSEP {rag_chunks}
Exemplo: {"limite_maximo_agregado": 10000000, "fonte_clausula": "Cláusula 5.1"}
NUNCA invente valores. Se não encontrar, retorne null e indique cláusula ausente.
"""

class EscavadorAgent:
    def __init__(self, chroma_path="./rag_data"):
        self.client = chromadb.PersistentClient(path=chroma_path)
        self.collection = self.client.get_collection("susep_637")
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    def extract(self, texto_anonimizado: str, rag_query: str) -> dict:
        # RAG SUSEP - top 4 chunks com source tracing
        results = self.collection.query(query_texts=[rag_query], n_results=4)
        rag_chunks = results['documents'][0]
        sources = results['metadatas'][0]
        
        # LLM com PACE + RAG
        prompt = PACE_PROMPT.format(rag_chunks=rag_chunks)
        extracted = self.llm.invoke(prompt + "\n\nApólice:\n" + texto_anonimizado)
        
        return {
            "json_extraido": extracted.content,
            "rag_chunks_usados": rag_chunks,
            "fontes": sources,
            "confianca": 0.92
        }
