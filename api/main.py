from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
import json
import os
import time

app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for real-time heart disease risk prediction",
    version="1.0.0"
)

# --------------------------------------------------
# Configuration
# --------------------------------------------------

ENDPOINT_NAME = os.getenv(
    "SAGEMAKER_ENDPOINT_NAME",
    "heart-disease-prod"
)
region =  'ap-southeast-1'
SAGEMAKER_ENDPOINT_NAME = 'team01-credit-card-fraud-ep'
runtime = boto3.client("sagemaker-runtime",region_name=region)


# --------------------------------------------------
# Request Model
# --------------------------------------------------

class HeartDiseaseRequest(BaseModel):

    State: str
    Sex: str
    GeneralHealth: str

    PhysicalHealthDays: float
    MentalHealthDays: float

    LastCheckupTime: str | None = None
    PhysicalActivities: str

    SleepHours: float

    RemovedTeeth: str | None = None

    HadAngina: str
    HadStroke: str
    HadAsthma: str
    HadSkinCancer: str
    HadCOPD: str
    HadDepressiveDisorder: str
    HadKidneyDisease: str
    HadArthritis: str
    HadDiabetes: str

    DeafOrHardOfHearing: str
    BlindOrVisionDifficulty: str
    DifficultyConcentrating: str
    DifficultyWalking: str
    DifficultyDressingBathing: str
    DifficultyErrands: str

    SmokerStatus: str
    ECigaretteUsage: str

    ChestScan: str

    RaceEthnicityCategory: str
    AgeCategory: str

    HeightInMeters: float | None = None
    WeightInKilograms: float | None = None
    BMI: float | None = None

    AlcoholDrinkers: str
    HIVTesting: str
    FluVaxLast12: str
    PneumoVaxEver: str
    TetanusLast10Tdap: str | None = None

    HighRiskLastYear: str
    CovidPos: str


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/")
def health_check():

    return {
        "status": "UP",
        "service": "Heart Disease Prediction API"
    }


# --------------------------------------------------
# Prediction
# --------------------------------------------------

@app.post("/predict")
def predict(request: HeartDiseaseRequest):

    try:

        start_time = time.time()

        # Convert request to dictionary
        payload = request.model_dump()

        # Send to SageMaker
        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType="application/json",
            Body=json.dumps(payload)
        )

        result = response["Body"].read().decode("utf-8")

        latency = round(
            (time.time() - start_time) * 1000,
            2
        )

        return {
            "prediction": result,
            "model_endpoint": ENDPOINT_NAME,
            "latency_ms": latency
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )