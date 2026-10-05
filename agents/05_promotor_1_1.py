
"""
Agente 5 - Promotor - Ataca cobertura (adversarial)
Aula 17 Multiagentes
"""
class PromotorAgent:
    def atacar(self, sinistro: dict, apolice: dict) -> dict:
        """
        sinistro: {"tipo": "CVM_insider", "descricao": "Diretor investigado por insider trading"}
        """
        # Baseado em exclusões reais + jurisprudência
        if sinistro['tipo'] == 'CVM_insider':
            return {
                "argumento": "Exclusão 4.2.a - Ato doloso + Insider Trading não coberto conforme STJ REsp 1.601.555",
                "clausula": apolice['exclusoes']['insider_trading']['clausula'],
                "jurisprudencia": "STJ 3a Turma - insider trading é ato doloso, fora do D&O",
                "prob_negacao": 0.85
            }
        if sinistro['tipo'] == 'LGPD':
            return {
                "argumento": "Multa LGPD é sanção regulatória, não dano a terceiro, sublimite não cobre",
                "clausula": apolice['limites']['sublimites']['multa_LGPD'].get('fonte_clausula'),
                "prob_negacao": 0.60
            }
        return {"argumento": "Exclusão genérica", "prob_negacao": 0.5}
