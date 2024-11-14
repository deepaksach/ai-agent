AI Chat Agent with Cryptocurrency Price Fetching

This project is a Flask-based AI chat agent that can:

Respond to user messages using Together AI's LLaMA API.
Fetch and provide real-time cryptocurrency prices (Bitcoin) using the CoinDesk API.
Features
AI-powered responses through Together AI's LLaMA model.
Cryptocurrency price fetching capability (Bitcoin) using CoinDesk API.
Simple API setup for easy integration and expansion.
Project Structure
app.py: Main server file that sets up the Flask app and defines the /ask endpoint.
agent.py: Defines the Agent class responsible for generating responses, including calling Together AI's LLaMA API and handling cryptocurrency queries.
crypto_api.py: A helper file for fetching the latest Bitcoin price using CoinDesk's API.
config.py: Stores the Together API Key (TOGETHER_API_KEY).
Requirements
Python 3.x
Flask
Requests library
