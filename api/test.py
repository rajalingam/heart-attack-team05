import requests

url = "https://hardened-triceps-handbook.ngrok-free.dev/predict"
headers = {
    "x-api-key": "team05-demo-key",
    "Content-Type": "application/json"
}

payload = {
    "State": "Texas",
    "Sex": "Female",
    "GeneralHealth": "Fair",
    "PhysicalHealthDays": 15.0,
    "MentalHealthDays": 30.0,
    "LastCheckupTime": "Within past year (anytime less than 12 months ago)",
    "PhysicalActivities": "Yes",
    "SleepHours": 4.0,
    "RemovedTeeth": "6 or more, but not all",
    "HadAngina": "No",
    "HadStroke": "No",
    "HadAsthma": "No",
    "HadSkinCancer": "No",
    "HadCOPD": "Yes",
    "HadDepressiveDisorder": "Yes",
    "HadKidneyDisease": "No",
    "HadArthritis": "Yes",
    "HadDiabetes": "No",
    "DeafOrHardOfHearing": "No",
    "BlindOrVisionDifficulty": "Yes",
    "DifficultyConcentrating": "No",
    "DifficultyWalking": "Yes",
    "DifficultyDressingBathing": "No",
    "DifficultyErrands": "No",
    "SmokerStatus": "Current smoker - now smokes every day",
    "ECigaretteUsage": "Never used e-cigarettes in my entire life",
    "ChestScan": "No",
    "RaceEthnicityCategory": "White only, Non-Hispanic",
    "AgeCategory": "Age 65 to 69",
    "HeightInMeters": 1.68,
    "WeightInKilograms": 48.53,
    "BMI": 17.27,
    "AlcoholDrinkers": "Yes",
    "HIVTesting": "No",
    "FluVaxLast12": "No",
    "PneumoVaxEver": "Yes",
    "TetanusLast10Tdap": "No, did not receive any tetanus shot in the past 10 years",
    "HighRiskLastYear": "No",
    "CovidPos": "No"
}

response = requests.post(url, headers=headers, json=payload, timeout=60)
print(response.status_code)
print(response.text)
