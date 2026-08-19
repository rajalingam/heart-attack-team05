
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import boto3
import json
import os

REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
ENDPOINT_NAME = os.environ.get("ENDPOINT_NAME", "heart-attack-team05-s502-endpoint")
RELAY_API_KEY = os.environ.get("RELAY_API_KEY", "team05-demo-key")

runtime = boto3.client("sagemaker-runtime", region_name=REGION)

app = FastAPI(title="Team05 SageMaker Endpoint Relay")

# For temporary demo use. For production, restrict allowed_origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "status": "running",
        "service": "Team05 FastAPI relay",
        "endpoint": ENDPOINT_NAME,
        "routes": ["GET /health", "POST /predict", "GET /docs"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(request: Request, x_api_key: str = Header(None)):
    if x_api_key != RELAY_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Request body must be valid JSON")

    # Keep the relay narrow: call only the fixed endpoint configured on the server side.
    try:
        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType="application/json",
            Accept="application/json",
            Body=json.dumps(payload)
        )

        result = response["Body"].read().decode("utf-8")

        try:
            return json.loads(result)
        except Exception:
            return {"raw_result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
