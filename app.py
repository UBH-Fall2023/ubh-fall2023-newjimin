from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    feeling_level = int(request.form['feelingSlider'])
    confidence_level = int(request.form['confidenceSlider'])
    
    academic_pressure = 'academicPressureCheckbox' in request.form
    personal_relationships = 'personalRelationshipsCheckbox' in request.form
    time_management = 'timeManagementCheckbox' in request.form
    health_and_safety = 'healthandsafetyCheckbox' in request.form

    advice = calculate_advice(feeling_level, confidence_level, academic_pressure, personal_relationships, time_management, health_and_safety)

    return render_template('results.html', advice=advice)

def calculate_advice(feeling_level, confidence_level, academic_pressure, personal_relationships, time_management, health_and_safety):
    advice = ''
    if feeling_level <= 33:
        if confidence_level <= 33:
            advice += 'Start small. Break tasks into manageable steps and celebrate each achievement. Seek support from peers, mentors, or counseling services. Focus on self-care activities to boost mood.<br>'
        elif confidence_level <= 67:
            advice += 'Recognize your emotions without judgment. Set realistic goals and prioritize self-care. Engage in activities that bring joy and relaxation. Consider seeking guidance from a mentor or counselor to address confidence concerns.<br><br>'
        else:
            advice += 'Reflect on the factors contributing to your low mood. While maintaining confidence, allow yourself to acknowledge and address emotions. Consider setting aside time for activities that bring emotional well-being. Seek support if needed.<br><br>'
    elif feeling_level <= 67:
        if confidence_level <= 33:
            advice += 'Embrace a growth mindset. Set small, achievable goals to build confidence gradually. Seek feedback and acknowledge your progress. Engage in activities that bring fulfillment and consider reaching out to a mentor or counselor for support.<br><br>'
        elif confidence_level <= 67:
            advice += 'Maintain balance. Continue your current routine while incorporating opportunities for personal growth. Regularly check in with your emotions and confidence levels. Seek support or advice when faced with challenges.<br><br>'
        else:
            advice += 'Continue your proactive approach. Set challenging yet attainable goals. Use your confidence to explore new opportunities for personal and academic growth. Remember to check in with your emotional well-being and seek support if needed.<br><br>'
    else:
        if confidence_level <= 33:
            advice += 'Acknowledge and embrace your positive emotions. Challenge negative self-talk and focus on your strengths. Gradually step outside your comfort zone, seeking support when needed. Celebrate achievements to boost confidence.<br><br>'
        elif confidence_level <= 67:
            advice += 'Leverage your positive emotions to explore new challenges. Set ambitious yet realistic goals. Acknowledge your accomplishments to build confidence. Regularly assess your emotional well-being and make adjustments as needed.<br><br>'
        else:
            advice += 'Celebrate your positive emotional state and confidence. Channel your energy into meaningful projects. Continue setting and achieving ambitious goals. Prioritize self-care to maintain a healthy balance. Share your positive experiences with others.<br><br>'

    if academic_pressure:
        advice += 'Academic Pressure: Embrace a growth mindset. View challenges as opportunities for learning and growth rather than stressors. Break down tasks into smaller, manageable steps. Seek academic support resources, such as study groups or workshops, to enhance your skills and confidence.<br><br>'

    if personal_relationships:
        advice += 'Personal Relationships: Foster open communication in your relationships. Actively listen to others, express your thoughts, and resolve conflicts constructively. Prioritize quality time with loved ones. Set healthy boundaries to maintain balance between your personal and academic life.<br><br>'

    if time_management:
        advice += 'Time Management: Develop a personalized time management strategy. Identify your priorities and allocate time accordingly. Utilize productivity tools and techniques to organize tasks. Regularly reassess and adjust your schedule to maintain a healthy balance between academic and personal commitments.<br><br>'

    if health_and_safety:
        advice += 'Health and Safety: Prioritize your well-being. Establish consistent self-care habits, including sufficient sleep, regular exercise, and a balanced diet. Stay informed about health and safety practices. Seek professional help when needed, and encourage a culture of well-being in your community.<br><br>'

    return advice

if __name__ == '__main__':
    app.run(debug=True)
