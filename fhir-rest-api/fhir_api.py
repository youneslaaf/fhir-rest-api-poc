from fastapi import FastAPI, HTTPException
import uvicorn

# Erstelle die API-Anwendung
app = FastAPI(
    title="Klinik FHIR API", 
    description="REST-API zur Abfrage von Patientendaten im HL7-FHIR-Format"
)

# Dummy-Datenbank (Simuliert ein lokales Krankenhausinformationssystem - KIS)
patients_db = {
    "1001": {
        "resourceType": "Patient",
        "id": "1001",
        "name": [{"family": "Mustermann", "given": ["Max"]}],
        "gender": "male",
        "birthDate": "1980-01-01"
    },
    "1002": {
        "resourceType": "Patient",
        "id": "1002",
        "name": [{"family": "Schmidt", "given": ["Anna"]}],
        "gender": "female",
        "birthDate": "1992-05-15"
    }
}

@app.get("/")
def read_root():
    return {"message": "Willkommen zur Medizininformatik FHIR-API. Gehe zu /docs für die interaktive API-Dokumentation."}

@app.get("/Patient/{patient_id}")
def get_patient(patient_id: str):
    """Gibt die FHIR-Daten eines spezifischen Patienten anhand der ID zurück."""
    if patient_id in patients_db:
        return patients_db[patient_id]
    
    # Fehler werfen, wenn Patient nicht existiert
    raise HTTPException(status_code=404, detail="Patient nicht im System gefunden")

if __name__ == "__main__":
    # Server lokal starten
    uvicorn.run(app, host="127.0.0.1", port=8000)