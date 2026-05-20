from fastapi import FastAPI, HTTPException
from circuitbreaker import CircuitBreaker
from llmservice import LLMService
from middleware import StudentIDMiddleware

app = FastAPI()

# Middleware
app.add_middleware(StudentIDMiddleware)

# Services
breaker = CircuitBreaker(
    failure_threshold=3,
    recovery_timeout=10
)

llm_service = LLMService()


@app.get("/")
def home():
    return {
        "message": "StudySync Circuit Breaker Running"
    }


@app.get("/generate")
def generate(prompt: str):

    # 1. Check circuit state
    if not breaker.call_allowed():
        return {
            "status": "fallback",
            "message": "AI service temporarily unavailable. Please try again later.",
            "circuit_state": breaker.state
        }

    try:
        # 2. Call LLM service
        response = llm_service.generate_response(prompt)

        # 3. Record success
        breaker.record_success()

        return {
            "status": "success",
            "data": {
                "response": response
            },
            "circuit_state": breaker.state
        }

    except Exception as e:
        # 4. Record failure
        breaker.record_failure()

        # IMPORTANT FIX:
        # Do NOT crash using HTTPException incorrectly
        # Instead return proper API response OR raise correctly

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )