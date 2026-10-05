
"""
Agente 6 - Defensor - Defende segurado
Aula 17 Multiagentes
"""
class DefensorAgent:
    def defender(self, sinistro: dict, apolice: dict, ataque_promotor: dict) -> dict:
        if sinistro['tipo'] == 'CVM_insider':
            return {
                "contra_argumento": "Cobertura A protege patrimônio pessoal do diretor, investigação CVM sem condenação não configura dolo. Cláusula 2.1.c garante custos de defesa desde notificação",
                "clausula_defesa": apolice['coberturas']['cobertura_A'],
                "jurisprudencia_favoravel": "STJ - custos de defesa devidos mesmo em investigação preliminar",
                "prob_cobertura": 0.70
            }
        return {"contra_argumento": "Cobertura ampla D&O", "prob_cobertura": 0.6}
