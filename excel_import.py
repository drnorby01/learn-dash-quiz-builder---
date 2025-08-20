import pandas as pd

def import_questions_from_excel(file_path):
    # Normalize column names
    df = pd.read_excel(file_path)
    df.columns = [col.strip().lower() for col in df.columns]

    questions = []

    for _, row in df.iterrows():
        question_text = str(row.get('question text', '')).strip()
        incorrect_feedback = str(row.get('incorrect feedback', '')).strip()

        if incorrect_feedback.lower() == 'nan':
            incorrect_feedback = ''

        # Extract answers
        answers = []
        for i in range(1, 10):  # Support up to 9 answers
            key = f'answer {i}'
            if key in row:
                answer_text = str(row.get(key, '')).strip()
                if answer_text and answer_text.lower() != 'nan':
                    answers.append(answer_text)

        # Validate correct index
        try:
            correct_index = int(row.get('correct index', -1))
        except (ValueError, TypeError):
            correct_index = -1

        if correct_index < 0 or correct_index >= len(answers):
            correct_index = 0  # fallback to first answer

        # Skip malformed rows
        if not question_text or len(answers) < 2:
            print(f"⚠️ Skipping row due to missing question or insufficient answers:\n{row}")
            continue

        questions.append({
            'question': question_text,
            'answers': answers,
            'correct_index': correct_index,
            'incorrect_feedback': incorrect_feedback
        })

    return {
        'title': 'Imported Quiz',
        'questions': questions
    }
