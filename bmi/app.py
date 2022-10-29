from fastapi import FastAPI
from starlette.responses import JSONResponse
import uvicorn
import os

app = FastAPI()
@app.post('/bmi')
async def analyze(features: dict):
    h = features['height']
    w = features['weight']
    # age = features['age']
    bmi = w*10000/(h*h)
    print(bmi,w,h)
    if(bmi>30):
        category='Obese'
    elif(bmi>25):
        category='Pre-Obesity'
    elif(bmi>18.5):
        category='Normal'
    else:
        category='Underweight'
    response ="Your BMI is {0:.2f} and your category is {1}".format(bmi, category)
    return JSONResponse({'response': response})

@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Iris classifier is all ready to go!'

port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    uvicorn.run(app, port=port, host='0.0.0.0')