import pandas as pd

def import_questions_from_excel(file_path):
    try:
        # Load Excel file
        df = pd.read_excel(file_path)

        # Normalize column names (lowercase, stripped)
        df.columns = [col.strip().lower() for col in df.columns]

        # Fill NaNs with empty strings to avoid attribute errors
        df.fillna('', inplace=True)

        questions = []

        for index, row in df.iterrows():
            # Defensive parsing of correct index
            try:
                correct_index = int(row.get('correct answer index', -1))
                if correct_index not in [0, 1, 2, 3]:
                    raise ValueError
            except (ValueError, TypeError):
                correct_index = -1  # Invalid index fallback

            # Clean feedback fields
            correct_feedback = str(row.get('correct feedback', '')).strip()
            incorrect_feedback = str(row.get('incorrect feedback', '')).strip()

            # Treat 'nan' as empty
            if correct_feedback.lower() == 'nan':
                correct_feedback = ''
            if incorrect_feedback.lower() == 'nan':
                incorrect_feedback = ''

            # Build question dictionary
            question = {
                'question': str(row.get('question text', '')).strip(),
                'answers': [
                    str(row.get('answer 1', '')).strip(),
                    str(row.get('answer 2', '')).strip(),
                    str(row.get('answer 3', '')).strip(),
                    str(row.get('answer 4', '')).strip()
                ],
                'correct_index': correct_index,
                'correct_feedback': correct_feedback,
                'incorrect_feedback': incorrect_feedback
            }

            questions.append(question)

        return questions

    except Exception as e:
        # Log and re-raise for Flask to catch
        print(f"Error importing Excel file: {e}")
        raise
