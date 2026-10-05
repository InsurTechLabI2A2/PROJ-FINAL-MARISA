
"""
Treino IA Clássica - RandomForest para score completude
Aula 12/13 IA Clássica - Dataset sintético 200 apólices rotuladas
Features: limite, sublimite_CVM, sublimite_LGPD, franquia, retroatividade, extensões
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from pathlib import Path

# Dataset sintético - 200 apólices rotuladas por domain expert Rogério
data = {
    "limite_max": [10,15,5,20,10]*40,
    "sublimite_CVM": [0,500,0,1000,0]*40,
    "sublimite_LGPD": [200,500,100,500,0]*40,
    "tem_custos_fora_limite": [0,1,0,1,0]*40,
    "tem_extensao_subsidiaria": [0,1,1,1,0]*40,
    "completo": [0,1,0,1,0]*40
}
df = pd.DataFrame(data)
X = df.drop("completo", axis=1)
y = df["completo"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

Path("models").mkdir(exist_ok=True)
joblib.dump(model, "models/completude_v1.pkl")
print(f"Acurácia: {model.score(X_test, y_test):.2f} - Modelo salvo em models/completude_v1.pkl")
print("Features importance:", dict(zip(X.columns, model.feature_importances_)))
