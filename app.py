from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    if length < 4:
        return "Erreur: longueur trop petite."

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = lowercase + uppercase + numbers + special_chars

    if not all_chars:
        return "Erreur: aucun ensemble de caractères choisi."

    password = [random.choice(lowercase)]
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special_chars:
        password.append(random.choice(special_chars))

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    length = int(data.get('length', 12))
    use_uppercase = data.get('uppercase', True)
    use_numbers = data.get('numbers', True)
    use_special_chars = data.get('special', True)

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)