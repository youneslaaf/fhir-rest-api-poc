# 🏥 HL7 FHIR REST-API (Proof of Concept)

Dieses Projekt ist ein Proof of Concept (PoC) zur Bereitstellung einer RESTful API für den standardisierten Austausch von Gesundheitsdaten. Entwickelt mit Python und dem FastAPI-Framework.

## 📌 Über das Projekt
Im modernen Krankenhausumfeld ist die Interoperabilität zwischen verschiedenen IT-Systemen (KIS, RIS, PACS) eine der größten Herausforderungen. Dieses Projekt simuliert eine standardisierte Schnittstelle, die Patientendaten aus einer fiktiven Datenbank im **HL7 FHIR-Standard** (Fast Healthcare Interoperability Resources) als JSON-Ressource bereitstellt.

Das Projekt demonstriert Kenntnisse in:
* **Systemintegration & Interoperabilität:** Verständnis von eHealth-Standards (HL7 FHIR).
* **Backend-Entwicklung:** Aufbau einer asynchronen REST-API mit Python (FastAPI).
* **Client-Server-Architektur:** HTTP-Methoden, Status-Codes und Routing.

## 🛠️ Tech-Stack
* **Sprache:** Python 3
* **Framework:** FastAPI, Uvicorn (ASGI Server)
* **Datenformat:** JSON (gemäß FHIR-Ressourcenstruktur)

## 🚀 Lokale Ausführung

1. **Repository klonen:**
   ```bash
   git clone https://github.com/youneslaaf/fhir-rest-api-poc.git
   cd fhir-rest-api-poc