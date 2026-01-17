from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def analyze_patient(msg):
    msg = msg.lower()

    urgency = "Low"

    high_words = ['emergency', 'severe', 'pain', 'bleeding', 'breathing', 'critical', 'suicide']
    mid_words = ['appointment', 'prescription', 'fever', 'checkup', 'transport']

    for w in high_words:
        if w in msg:
            urgency = "High"

    if urgency == "Low":
        for w in mid_words:
            if w in msg:
                urgency = "Medium"

    category = "General Inquiry"

    if 'sad' in msg or 'depressed' in msg or 'anxiety' in msg or 'lonely' in msg:
        category = "Mental Health Support"
    elif 'delivery' in msg or 'food' in msg or 'ride' in msg or 'money' in msg:
        category = "Logistics/Aid"
    elif 'doctor' in msg or 'nurse' in msg or 'medicine' in msg or 'pain' in msg:
        category = "Medical Consultation"

    if urgency == "High":
        auto_msg = "⚠️ URGENT: A coordinator has been notified via SMS. Call emergency services if in immediate danger."
    else:
        auto_msg = "✅ We have received your request. A volunteer will contact you within 24 hours."

    result = {
        "type": "patient_triage",
        "label": "Triage Category",
        "category": category,
        "tag_label": "Urgency",
        "tag_value": urgency,
        "auto_response": auto_msg
    }

    return result


def analyze_volunteer(msg):
    msg = msg.lower()

    team = "General Support Team"
    badge = "Community Helper"

    if 'doctor' in msg or 'nurse' in msg or 'md' in msg or 'rn' in msg:
        team = "Medical Response Team"
        badge = "🩺 Medical Pro"

    if 'drive' in msg or 'car' in msg or 'license' in msg:
        team = "Logistics & Transport"
        badge = "🚗 Driver"

    if 'call' in msg or 'listen' in msg or 'talk' in msg:
        team = "Tele-Counseling Team"
        badge = "🎧 Counselor"

    if 'code' in msg or 'tech' in msg or 'computer' in msg:
        team = "IT & Ops Team"
        badge = "💻 Tech Support"

    return {
        "type": "volunteer_match",
        "label": "Assigned Unit",
        "category": team,
        "tag_label": "Skill Badge",
        "tag_value": badge,
        "auto_response": "Welcome aboard! Based on your bio, we have drafted you into the " + team + ". An onboarding manager will email you."
    }


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json

    role = data.get("role")
    msg = data.get("message")

    if role == "Patient":
        analysis = analyze_patient(msg)
    else:
        analysis = analyze_volunteer(msg)

    return jsonify({
        "status": "success",
        "analysis": analysis
    })


if __name__ == "__main__":
    app.run(debug=True)
