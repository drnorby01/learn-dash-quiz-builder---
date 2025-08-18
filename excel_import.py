import gspread
from oauth2client.service_account import ServiceAccountCredentials

def import_questions_from_sheet(sheet_url):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(sheet_url).sheet1
    rows = sheet.get_all_records()

    questions = []
    for row in rows:
        questions.append({
            'question': row['Question Text'],
            'answers': [row['Answer 1'], row['Answer 2'], row['Answer 3'], row['Answer 4']],
            'correct_index': int(row['Correct Answer Index']),
            'correct_feedback': row['Correct Feedback'],
            'incorrect_feedback': row['Incorrect Feedback']
        })
    return questions
