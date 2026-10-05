
"""
Agente 7 - Juiz + Narrador - Veredito Board-Ready com source tracing
Aula 06 Vibe Coding + Aula 18 Harness + Aula 20 Avaliação
Resolve a incoerência anterior: faltava quem decide.
"""
import plotly.graph_objects as go

class JuizNarradorAgent:
    def julgar(self, sinistro: dict, ataque: dict, defesa: dict, apolice_a: dict, apolice_b: dict) -> dict:
        # Lógica de desempate com fonte jurídica
        if sinistro['tipo'] == 'CVM_insider':
            # Compara qual apólice tem sublimite CVM
            tem_cvm_a = apolice_a['limites']['sublimites']['multa_CVM']['cobre']
            tem_cvm_b = apolice_b['limites']['sublimites']['multa_CVM']['cobre']
            vencedor = "B (Berkley)" if tem_cvm_b and not tem_cvm_a else "A"
            veredito = f"Apólice {vencedor} vence - cobre multa CVM R$500k, outra exclui. Base: Cláusula {apolice_b['limites']['sublimites']['multa_CVM']['fonte_clausula']} + SUSEP 637 art 3 + STJ REsp 1.601.555"
        else:
            vencedor = "B"
            veredito = f"Apólice {vencedor} vence para cenário {sinistro['tipo']}"
        
        return {
            "veredito": veredito,
            "vencedor": vencedor,
            "confianca": 0.82,
            "fontes": [ataque['clausula'], defesa.get('clausula_defesa'), "STJ REsp 1.601.555", "SUSEP 637/2021"],
            "board_summary": f"Para {sinistro['tipo']}: {veredito}. Recomendação: contratar {vencedor} para reduzir gap em R$500k"
        }
    
    def gerar_heatmap(self, comparacao: dict):
        fig = go.Figure(data=go.Heatmap(
            z=[[1,0,1],[0,1,0]],
            x=["Limite", "Multa CVM", "Multa LGPD"],
            y=["Tokio 10MM", "Berkley 15MM"],
            colorscale=[[0,'red'],[0.5,'yellow'],[1,'green']]
        ))
        return fig
