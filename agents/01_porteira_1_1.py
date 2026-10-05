
"""
Agente 1 - Porteira - Ingestão Multimodal LGPD-First
Aula 07 Governança + Aula 20 Multimodal + Aula 22 Privacidade
Fluxo: Tesseract local -> Presidio -> Azure Document Intelligence (opcional, só após anonimização)
"""
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
import pytesseract
from PIL import Image

class PorteiraAgent:
    def __init__(self):
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()
    
    def process(self, file_path: str) -> dict:
        # 1. OCR local primeiro - nunca envia dado bruto para nuvem
        text_local = pytesseract.image_to_string(Image.open(file_path), lang='por') if file_path.endswith(('.png','.jpg')) else self._extract_pdf_local(file_path)
        
        # 2. Anonimização ANTES de qualquer LLM externa
        pii_results = self.analyzer.analyze(text=text_local, language='pt')
        anon_result = self.anonymizer.anonymize(text=text_local, analyzer_results=pii_results)
        
        return {
            "texto_anonimizado": anon_result.text,
            "pii_detectado": len(pii_results),
            "anonimizado": True,
            "fonte_ocr": "tesseract_local",
            "pronto_para_nuvem": True
        }
    
    def _extract_pdf_local(self, path): return "texto extraido localmente"
