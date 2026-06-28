from src.ai.ollama_client import ask_ai

prompt = """
Suggest an AI startup idea for a college student
who has ₹100000 budget and good programming skills.
"""

print(ask_ai(prompt))