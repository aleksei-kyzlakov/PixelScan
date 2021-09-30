import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import config
from pixelscan import task

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = 'super secret key'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('Отсутствует картинка')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('Картинка не выбрана')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Картинка загружена')
        task_result = task(filename)
        return render_template('upload.html', filename=filename, task_result=task_result)
    else:
        flash('Допустимые форматы -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='img/' + filename), code=301)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30006, debug=True)
