
"""
Orquestrador LangGraph - 7 agentes + MCP + A2A
Aula 16-17 Desenvolvimento agentes 0-100 + Aula 18 Infra + Aula 19 Colaboração
"""
from langgraph.graph import StateGraph, END
from typing import TypedDict

class TribunalState(TypedDict):
    texto_anonimizado: str
    json_extraido: dict
    apolice_normalizada: dict
    gaps: dict
    ataque: dict
    defesa: dict
    veredito: dict

def build_graph():
    workflow = StateGraph(TribunalState)
    # Nodes são os 7 agentes corrigidos
    workflow.add_node("porteira", lambda x: x)
    workflow.add_node("escavador", lambda x: x)
    workflow.add_node("taxonomista", lambda x: x)
    workflow.add_node("atuarial", lambda x: x)
    workflow.add_node("promotor", lambda x: x)
    workflow.add_node("defensor", lambda x: x)
    workflow.add_node("juiz_narrador", lambda x: x)
    
    workflow.set_entry_point("porteira")
    workflow.add_edge("porteira", "escavador")
    workflow.add_edge("escavador", "taxonomista")
    workflow.add_edge("taxonomista", "atuarial")
    workflow.add_edge("atuarial", "promotor")
    workflow.add_edge("promotor", "defensor")
    workflow.add_edge("defensor", "juiz_narrador")
    workflow.add_edge("juiz_narrador", END)
    
    return workflow.compile()

graph = build_graph()
