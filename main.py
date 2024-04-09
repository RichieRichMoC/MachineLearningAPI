from fastapi import FastAPI, HTTPException, Response
import joblib
from pydantic import BaseModel
import pandas as pd
import uvicorn

pipeline = joblib.load('./models/rf_classifier_pipeline.joblib')
pipeline2 = joblib.load('./models/tree_classifier_pipeline.joblib')
pipeline3 = joblib.load('./models/logistic_classifier_pipeline.joblib')
encoder = joblib.load('./models/label_encoder.joblib')

app = FastAPI()

class SepssisFeatures(BaseModel):
  PRG: int
  PL: int
  PR: int
  SK: int
  TS: int
  M11: float
  BD2: float
  Age: int
  Insurance: int



@app.get('/')
def home():
    return Response('Hello world')


@app.get('/info')
def appinfo():
    return Response('This is the info page of this API')


@app.post('/predict_Sepssis_with_rf_classifier')
def predict_Sepssis(sepssis_features: SepssisFeatures):

    try: 
    
        df = pd.DataFrame([sepssis_features.model_dump()])

        prediction = pipeline.predict(df)

        decoded_prediction = encoder.inverse_transform([prediction])[0]

        return {'prediction': decoded_prediction}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'This is a server error {str(e)}')



@app.post('/predict_Sepssis_with_tree_classifier')
def predict_Sepssis(sepssis_features2: SepssisFeatures):

    try: 
    
        df = pd.DataFrame([sepssis_features2.model_dump()])

        prediction2 = pipeline2.predict(df)

        decoded_prediction2 = encoder.inverse_transform([prediction2])[0]

        return {'prediction': decoded_prediction2}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'This is a server error {str(e)}')
    

    
@app.post('/predict_Sepssis_with_logistic_classifier')
def predict_Sepssis(sepssis_features3: SepssisFeatures):

    try: 
    
        df = pd.DataFrame([sepssis_features3.model_dump()])

        prediction3 = pipeline3.predict(df)

        decoded_prediction3 = encoder.inverse_transform([prediction3])[0]

        return {'prediction': decoded_prediction3}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'This is a server error {str(e)}')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)