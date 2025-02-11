from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib
import numpy as np
from model import IrisFeatures

app = FastAPI(title="Iris Prediction App")

templates = Jinja2Templates(directory="templates")

# Load or train the model
try:
    model = joblib.load('iris_model.joblib')
except:
    from train import train_model
    train_model()
    model = joblib.load('iris_model.joblib')

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(features: IrisFeatures):
    try:
        feature_array = np.array([[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]])
        
        prediction = model.predict(feature_array)
        iris_classes = ['setosa', 'versicolor', 'virginica']
        predicted_class = iris_classes[prediction[0]]
        
        return {
            "prediction": predicted_class,
            "probability": float(model.predict_proba(feature_array).max())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
