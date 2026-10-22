import pickle
from fastapi import FastAPI
# from pydantic import BaseModel

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# class Customer(BaseModel):
#     gender: str
#     seniorcitizen: int
#     partner: str
#     dependents: str
#     tenure: int
#     phoneservice: str
#     multiplelines: str
#     internetservice: str
#     onlinesecurity: str
#     onlinebackup: str
#     deviceprotection: str
#     techsupport: str
#     streamingtv: str
#     streamingmovies: str
#     contract: str
#     paperlessbilling: str
#     paymentmethod: str
#     monthlycharges: float
#     totalcharges: float

app = FastAPI(title="Churn Prediction Service", version="1.0")

@app.get("/")
def home():
    return {"message": "Churn Model API is running."}

@app.post("/predict")
def predict(customer: dict):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = bool(y_pred >= 0.5)
    
    return {
        "churn_probability": float(y_pred),
        "churn": churn
    }

# @app.post("/predict")
# def predict(customer: Customer):
#     customer_dict = customer.model_dump()
    
#     X = dv.transform([customer_dict])
#     y_pred = model.predict_proba(X)[0, 1]
#     churn = bool(y_pred >= 0.5)
    
#     return {
#         "churn_probability": float(y_pred),
#         "churn": churn
#     }