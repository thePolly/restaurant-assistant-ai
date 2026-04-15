# AI Restaurant Assistant

AI-powered assistant for handling restaurant reservations using natural language.

This project is being developed for a restaurant in Switzerland, where customers typically make reservations via email. The goal is to automate request processing, availability checking, and response generation.

## Current Status (MVP)

This project is in progress.

In the current version:
- reservation requests are entered manually (via API or terminal)
- the system processes the request
- checks availability based on stored data
- generates a response in German

Email integration and frontend are planned next.

## Core Idea

The assistant simulates how a restaurant handles reservation requests:

1. A customer sends a request (e.g. “Table for 2 at 19:00 near the window”)
2. The system extracts structured data from the message
3. It checks availability of the requested seating
4. It generates a polite response in German:
   - confirms the reservation if available
   - suggests alternatives if not

## Architecture (MVP)

Client (terminal or API)
    ↓
FastAPI endpoint
    ↓
Reservation flow (LangChain and business logic)
    ↓
Availability check (JSON data)
    ↓
German response generation

## Tech Stack

Backend:
- Python
- FastAPI
- LangChain

Frontend (planned):
- React
- TypeScript

## Planned Features

- Email integration for reading and replying to reservation requests
- Web interface for customers (React frontend)
- Real-time table availability view
- Admin interface for restaurant staff:
  - manual reservation management
  - editing availability
- Persistent database instead of JSON storage

## How to Run

1. Install dependencies:

pip install -r requirements.txt
2. Run the server:
uvicorn main:app --reload
3. Test the API:

POST request to:
http://127.0.0.1:8000/process-email

Example request body:
{
"message": "Guten Tag, ich möchte morgen um 19 Uhr einen Tisch für 2 Personen am Fenster reservieren."
}

## Project Structure

restaurant-assistant/
├── main.py
├── reservation_flow.py
├── prompts.py
├── reservations.json
├── requirements.txt
└── README.md
