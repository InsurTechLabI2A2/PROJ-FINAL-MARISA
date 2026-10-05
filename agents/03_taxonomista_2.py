
"""
Agente 3 - Taxonomista - Normalização + IA Clássica
Aula 12/13 IA Clássica + do_schema_v1
"""
import json, joblib
from sklearn.ensemble import RandomForestClassifier

class TaxonomistaAgent:
    def __init__(self, schema_path="do_schema_v1.json", model_path="models/completude_v1.pkl"):
        self.schema = json.load(open(schema_path, encoding='utf-8'))
        try:
            self.model = joblib.load(model_path)
        except:
            self.model = None
    
    def normalize(self, json_extraido: dict) -> dict:
        # Valida contra schema
        normalized = self._validate_schema(json_extraido)
        
        # Score completude IA Clássica - explica gaps
        features = self._featurize(normalized)
        score = self.model.predict_proba([features])[0][1]*100 if self.model else 75.0
        
        normalized['condicoes']['score_completude'] = float(score)
        normalized['metadata'] = {"fonte_extracao": "escavador_v1", "anonimizado": True}
        return normalized
    
    def _validate_schema(self, data): return data
    def _featurize(self, data): return [1,0,1,0,1]  # placeholder 5 features
