from src.ai.ollama_client import ask_ai


def generate_founder_advice(founder_data):

    prompt = f"""
You are an expert startup mentor.

Analyze this founder:

Name: {founder_data['name']}
Age: {founder_data['age']}
Education: {founder_data['education']}
Occupation: {founder_data['occupation']}

Budget: ₹{founder_data['budget']}
Team Size: {founder_data['team_size']}

Programming: {founder_data['programming']}/10
Marketing: {founder_data['marketing']}/10
Finance: {founder_data['finance']}/10
Leadership: {founder_data['leadership']}/10
Communication: {founder_data['communication']}/10
Problem Solving: {founder_data['problem_solving']}/10
Risk Tolerance: {founder_data['risk_tolerance']}/10

Startup Stage:
{founder_data['startup_stage']}

Founder Score:
{founder_data['score']}

Give:

1. Overall assessment
2. Best startup category
3. Biggest weakness
4. Next 30-day action plan

Keep the response under 250 words.
"""

    return ask_ai(prompt)