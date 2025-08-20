from flask import Flask, render_template, request, send_file, jsonify
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
    file = request.files.get('excel_file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    imported = import_questions_from_excel(file_path)
    return jsonify(imported)

@app.route('/export', methods=['POST'])
def export_quiz():
    data = request.get_json()
    if not data or 'questions' not in data:
        return jsonify({'error': 'Invalid payload'}), 400

    filename = generate_quiz_xml(data)

    # Serve the XML file as a download
    return send_file(filename, mimetype='application/xml', as_attachment=True)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
