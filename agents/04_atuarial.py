
"""
Agente 4 - Atuarial - Gap Analysis Técnico
Aula 02 Gestão de Riscos
"""
class AtuarialAgent:
    def compare(self, apolice_a: dict, apolice_b: dict) -> dict:
        gaps = []
        # Compara sublimites críticos
        for key in ["multa_CVM", "multa_LGPD", "custos_defesa"]:
            val_a = apolice_a.get('limites',{}).get('sublimites',{}).get(key,{}).get('valor',0)
            val_b = apolice_b.get('limites',{}).get('sublimites',{}).get(key,{}).get('valor',0)
            if val_a != val_b:
                gaps.append({
                    "campo": key,
                    "apolice_A": val_a,
                    "apolice_B": val_b,
                    "criticidade": "ALTA" if key=="multa_CVM" else "MEDIA",
                    "fonte_clausula_A": apolice_a.get('limites',{}).get('sublimites',{}).get(key,{}).get('fonte_clausula'),
                    "fonte_clausula_B": apolice_b.get('limites',{}).get('sublimites',{}).get(key,{}).get('fonte_clausula')
                })
        return {"gaps": gaps, "score_A": apolice_a['condicoes']['score_completude'], "score_B": apolice_b['condicoes']['score_completude']}
