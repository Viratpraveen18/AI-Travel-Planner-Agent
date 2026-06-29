from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():

    destination = request.form['destination']
    budget = request.form['budget']
    days = request.form['days']
    interests = request.form['interests']

    prompt = f"""
    Create a travel itinerary.

    Destination: {destination}
    Budget: {budget}
    Number of Days: {days}
    Interests: {interests}

    Include:

    Day-wise itinerary
    Tourist attractions
    Food recommendations
    Hotel suggestions
    Estimated expenses
    Travel tips
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    plan = response.choices[0].message.content

    return render_template(
        "index.html",
        result=plan
    )


if __name__ == "__main__":
    app.run(debug=True)
  
