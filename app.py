from flask import Flask, render_template, request, send_file, redirect, url_for
import requests, os, tempfile

app = Flask(__name__)
API_KEY = os.getenv("SMALLPDF_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_pdf():
    if 'file' not in request.files:
        return redirect(url_for('home'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('home'))

    url = "https://api.smallpdf.com/v1/pdf2word"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    files = {
        'file': (file.filename, file.stream, file.mimetype)
    }

    resp = requests.post(url, headers=headers, files=files, stream=True)
    if resp.status_code == 200:
        suffix = '.docx'
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        with open(tmp.name, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return send_file(tmp.name, as_attachment=True, download_name='converted.docx')
    else:
        return f"Error from Smallpdf API: {resp.status_code} - {resp.text}", 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
