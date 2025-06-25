# app.py
from flask import Flask, request, render_template, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)
engine = create_engine("sqlite:///animals.db")

@app.route('/')
def index():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT DISTINCT Animal FROM animals WHERE Animal IS NOT NULL"))
        animal_names = sorted([row[0] for row in result])
    return render_template('index.html', animal_names=animal_names)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    animal_name = data.get('animal_name', '').strip().lower()

    query = text("SELECT * FROM animals WHERE LOWER(Animal) = :name")
    with engine.connect() as conn:
        result = conn.execute(query, {'name': animal_name}).mappings().first()

    if result:
        result_dict = dict(result)
        return jsonify(result_dict)
    else:
        return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
