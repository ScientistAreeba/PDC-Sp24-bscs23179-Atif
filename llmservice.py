import time
import random


class LLMService:
    def generate_response(self, prompt: str):

        # Simulate random failure
        failure = random.choice([True, False])

        if failure:
            print("LLM API Failed - Simulated")

            # Simulate slow timeout
            time.sleep(3)

            raise Exception("External LLM API Timeout")

        return {
            "response": f"Generated AI response for: {prompt}"
        }