# Areeba Atif - BSCS23179

## StudySync Circuit Breaker Assignment

This project demonstrates the implementation of the **Circuit Breaker Pattern** using:

* Python
* FastAPI
* Middleware
* Simulated LLM Service Failures

The system prevents continuous requests to a failing AI service by opening the circuit after multiple failures and returning fallback responses.

---

# Project Structure

```bash
bscs23179_assignment2/
│
├── main.py
├── circuitbreaker.py
├── llmservice.py
├── middleware.py
├── testfailure.py
├── requirements.txt
└── README.md
```

---

# Features

* FastAPI REST API
* Circuit Breaker Implementation
* Failure Threshold Handling
* Recovery Timeout Handling
* Middleware for Student ID Header
* Simulated External LLM API Failures
* Automated Failure Testing Script

---

# Requirements

Install Python 3.10 or above.

---

# Install Dependencies

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

## Windows

```bash
venv\Scripts\activate
```

## Linux / Mac

```bash
source venv/bin/activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

---

# Run the FastAPI Server

Start the server using:

```bash
uvicorn main:app --reload
```

Server will run at:

```bash
http://127.0.0.1:8000
```

---

# API Endpoints

## Home Endpoint

```http
GET /
```

Returns:

```json
{
  "message": "StudySync Circuit Breaker Running"
}
```

---

## Generate Endpoint

```http
GET /generate?prompt=your_prompt
```

Example:

```http
GET /generate?prompt=Explain Distributed Systems
```

Possible Responses:

### Success Response

```json
{
  "status": "success",
  "data": {
    "response": "Generated AI response"
  },
  "circuit_state": "CLOSED"
}
```

### Failure Response

```json
{
  "detail": "External LLM API Timeout"
}
```

### Fallback Response (Circuit Open)

```json
{
  "status": "fallback",
  "message": "AI service temporarily unavailable. Please try again later.",
  "circuit_state": "OPEN"
}
```

---

# Run Failure Testing Script

Open another terminal and activate the virtual environment again:

```bash
venv\Scripts\activate
```

Run the test script:

```bash
python testfailure.py
```

---

# Expected Test Behavior

* Initial requests succeed
* Simulated API failures occur
* After threshold failures, circuit becomes OPEN
* Requests return fallback responses
* Middleware adds custom student ID header

---

# Middleware Header

Every response contains:

```http
X-Student-ID: BSCS23179
```

---

# Circuit Breaker Working

## CLOSED State

* Requests are allowed
* Failures are monitored

## OPEN State

* Requests are blocked
* Fallback response returned

## HALF-OPEN State

* System tests if service has recovered

---

# Sample Output

```bash
Request #1 → Success
Request #2 → Success
Request #3 → Failure
Request #4 → Failure
Request #5 → Circuit OPEN
Request #6 → Fallback Response
```

---

# Technologies Used

* Python
* FastAPI
* Uvicorn
* Requests Library

---

# Author

## Areeba Atif

## BSCS23179
