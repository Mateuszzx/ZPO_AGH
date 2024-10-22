from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return 'testowy tekst'

('form action=image/method=post encryption=utf-8')


@app.route('/image', methods=["POST"])
def analyze_image():
    if 'image' not in request.files:
        return 'brak pliku'
    file = request.files['image']
    
    if file.filename == '':
        return 'plik jest pusty'
    
    if file.filename.split('.')[-1] == 'jpg':
        filename = secure_filename(file.filename)
        os.makedirs('./uploaded_files', exist_ok=True)
        file.save(f'.uploaded_files/{filename}')



if __name__ == '__main__':
    app.run(host='localhost', port=8080)