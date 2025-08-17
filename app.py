from flask import Flask, render_template, request, send_file
from sheets_import import import_questions_from_sheet
from xml_generator import generate_quiz_xml
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import', methods=['POST'])
def import_sheet():
    sheet_url = request.form['sheet_url']
    questions = import_questions_from_sheet(sheet_url)
    return {'questions': questions}

@app.route('/export', methods=['POST'])
def export_quiz():
    data = request.json
    filename = generate_quiz_xml(data)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
