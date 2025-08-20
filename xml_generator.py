import xml.etree.ElementTree as ET

def generate_quiz_xml(data):
    wpProQuiz = ET.Element('wpProQuiz')
    header = ET.SubElement(wpProQuiz, 'header', {
        'version': '0.29',
        'exportVersion': '1',
        'ld_version': '4.24.0',
        'LEARNDASH_SETTINGS_DB_VERSION': '2.5'
    })

    data_el = ET.SubElement(wpProQuiz, 'data')
    quiz = ET.SubElement(data_el, 'quiz')
    ET.SubElement(quiz, 'title', {'titleHidden': 'true'}).text = data['title']
    ET.SubElement(quiz, 'text').text = 'Progress Check'

    questions_el = ET.SubElement(quiz, 'questions')
    for i, q in enumerate(data['questions']):
        assert isinstance(q, dict), f"Expected question dict, got {type(q)}"

        question = ET.SubElement(questions_el, 'question', {'answerType': 'multiple'})
        ET.SubElement(question, 'title').text = f'Question {i+1}'
        ET.SubElement(question, 'points').text = '1'
        ET.SubElement(question, 'questionText').text = q['question']
        ET.SubElement(question, 'correctMsg').text = ''
        ET.SubElement(question, 'incorrectMsg').text = q['incorrect_feedback']

        answers_el = ET.SubElement(question, 'answers')
        for j, ans in enumerate(q['answers']):
            answer = ET.SubElement(answers_el, 'answer', {
                'points': '0',
                'correct': 'true' if j == q['correct_index'] else 'false'
            })
            ET.SubElement(answer, 'answerText', {'html': 'false'}).text = ans
            ET.SubElement(answer, 'stortText', {'html': 'false'}).text = ''

    tree = ET.ElementTree(wpProQuiz)
    filename = 'quiz_export.xml'
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    return filename
