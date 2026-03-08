# Real-Time Multilingual Voice AI Agent

This project implements a real-time voice AI agent that helps patients book, reschedule, and cancel clinical appointments using voice conversations.

## Features

- Voice-based appointment booking
- Appointment rescheduling
- Appointment cancellation
- Multilingual support (English, Hindi, Tamil)
- AI agent reasoning
- Contextual memory
- Real-time communication pipeline

## System Architecture

User Speech
↓
Speech-to-Text
↓
Language Detection
↓
AI Agent
↓
Tool Orchestration
↓
Appointment Service
↓
Text Response
↓
Text-to-Speech
↓
Audio Response

## Technologies Used

Python  
FastAPI  
OpenAI / LLM  
Redis  
PostgreSQL  
WebSockets

## Setup Instructions

1. Clone repository
git clone https://github.com/19NN1A05F5/2care.ai.git
cd 2care.ai

2. Install Dependencies
pip install -r requirements.txt

3. Run the Backend Server
uvicorn backend.main:app --reload

Server will start at:
http://localhost:8000
You can test the API using a browser or Postman.


## Memory Design

Session Memory (Redis)

Stores conversation context.

Example:
intent: booking
doctor: cardiologist
date: tomorrow


Persistent Memory (Database)

Stores long-term patient information such as:

- patient_id
- preferred_language
- past_appointments

## Latency Breakdown

Speech Recognition → 120 ms  
Agent Reasoning → 200 ms  
Speech Synthesis → 100 ms  

Total Target Latency:
< 450 ms

## Testing Scenarios

Book appointment → Appointment confirmed  
Cancel appointment → Booking removed  
Reschedule appointment → Slot updated  
Language switching → Agent adapts language  
Conflict booking → Alternative slot suggested
