from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import ocrmypdf
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/processed_pdfs'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# def ocr(file_path, save_path):
#     ocrmypdf.ocr(file_path, save_path, skip_text=True, color_conversion_strategy="RGB")
def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, skip_text=True, color_conversion_strategy="RGB")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file is submitted
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_' + file.filename)
            file.save(file_path)
            ocr(file_path, save_path)
            return redirect(url_for('uploaded_file', filename='processed_' + file.filename))
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)