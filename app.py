from flask import Flask, render_template, request, send_file
from excel_import import import_questions_from_excel
from xml_generator import generate_quiz_xml
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import', methods=['POST'])
def import_excel():
    file = request.files['excel_file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    questions = import_questions_from_excel(file_path)
    return {'questions': questions}

@app.route('/export', methods=['POST'])
def export_quiz():
    file = request.files['file']
    imported = import_questions_from_excel(file)

    # Ensure the structure matches what xml_generator expects
    data = {
        'title': imported.get('title', 'Exported Quiz'),
        'questions': imported.get('questions', [])
    }

    filename = generate_quiz_xml(data)
    return f"Quiz exported to {filename}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
