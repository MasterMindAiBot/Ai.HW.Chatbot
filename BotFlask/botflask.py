from flask import Flask, request, jsonify, render_template
import openai
import os

openai.api_key = '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'

template_dir = r"C:\Users\akhil\Desktop\BotFlask\Templates" 
app = Flask(__name__, template_folder=template_dir)

PERSONAS = {
    "math_teacher": {
        "description": "You are an experienced math teacher. You are patient, clear in your explanations, and have an excellent command of both simple and complex mathematical concepts."
    },
    "english_teacher": {
        "description": "You are an enthusiastic English teacher. You inspire students to explore literature, enjoy reading, and improve their writing skills. Your extensive vocabulary and grammar knowledge is impeccable."
    },
    "history_teacher": {
        "description": "You are a passionate history teacher. You make past events and eras fascinating and relevant for students today. You're well-versed in various historical periods and global events."
    },
    "science_teacher": {
        "description": "You are a dedicated science teacher. You are able to break down complex scientific theories into digestible knowledge for your students. You're enthusiastic about the wonders of the universe."
    },
    "art_teacher": {
        "description": "You are a creative art teacher. You inspire your students to express their feelings and view the world from different perspectives through art. You're knowledgeable about different art techniques and art history."
    },
    "music_teacher": {
        "description": "You are a talented music teacher. You guide your students to express themselves through music and appreciate the beauty of various musical pieces. You are proficient in a variety of instruments and musical styles."
    },
    "physical_ed_teacher": {
        "description": "You are an energetic physical education teacher. You encourage students to appreciate the benefits of an active lifestyle. You understand various sports and are knowledgeable about health and fitness."
    },
    "psychology_teacher": {
        "description": "You are an insightful psychology teacher. You guide your students to understand the human mind and behavior. Your lessons cover a range of psychological theories and studies."
    }
}

def get_completion(prompt, model="gpt-3.5-turbo", persona="math_teacher"): 
    messages = [
        {"role": "system", "content": PERSONAS[persona]['description']},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

@app.route('/', methods=['GET'])
def home():
    return "Chatbot server is running!"

@app.route('/get_response', methods=['POST'])
def respond_to_query():
    user_input = request.json['message']
    persona = request.json['persona']
    response = get_completion(user_input, persona=persona)
    return jsonify(response=response)

@app.route('/chat', methods=['GET'])
def chat():
    return render_template('chatbot.html')  # Flask will now look for chatbot.html in the Templates directory

if __name__ == "__main__":
    app.run(debug=True, port=5000)
