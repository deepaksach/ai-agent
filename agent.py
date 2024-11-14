# agent.py
import requests
from config import TOGETHER_API_KEY
from crypto_api import get_crypto_price

class Agent:
    def __init__(self):
        self.context = []  # Stores conversation history

    def call_llama_api(self, prompt):
        """Calls Together AI's LLaMA API to generate a response."""
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",  # Adjust model name if needed
            "prompt": prompt,
            "max_tokens": 50,
        }

        try:
            response = requests.post("https://api.together.ai/llama/v1/completions", headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["text"].strip()
        except requests.exceptions.RequestException as e:
            print(f"Error calling LLaMA API: {e}")
            return "Sorry, I'm having trouble generating a response right now."

    def handle_crypto_query(self, crypto_name):
        """Fetches and returns the current price of a cryptocurrency."""
        price = get_crypto_price()
        print('price', price)
        if price:
            return f"The current price of {crypto_name.capitalize()} is ${price}."
        return "Sorry, I couldn't fetch the price at the moment."

    def get_response(self, user_input):
        """Generates responses based on user input."""
        self.context.append(user_input)

        # Check if user asked about cryptocurrency prices
        if "price" in user_input.lower():
            if "bitcoin" in user_input.lower():
                return self.handle_crypto_query("bitcoin")
            else:
                return "Please specify which cryptocurrency's price you want to check."

        # For other questions, use LLaMA
        prompt = " ".join(self.context)
        return self.call_llama_api(prompt)
