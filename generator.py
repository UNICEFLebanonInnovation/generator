from flask import request
from flask.ext.api import FlaskAPI, status

from generate_id import generate_id

app = FlaskAPI(__name__)

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        id_number = generate_id(
            request.data.get('first_name', ''),
            request.data.get('father_name', ''),
            request.data.get('last_name', ''),
            request.data.get('mother_name', ''),
            request.data.get('gender', ''),
            request.data.get('birthday_day', ''),
            request.data.get('birthday_month', ''),
            request.data.get('birthday_year', '')
        )
        return {'hash': id_number}, status.HTTP_201_CREATED
    else:
        return {'message': 'Please use POST'}


if __name__ == '__main__':
    app.run()
