from flask import Flask, render_template, request, send_file
import qrcode
import io
import base64

# Point Flask to the designing folder
app = Flask(__name__, template_folder='designing')

@app.route('/')
def index():
    return render_template('index.html', qr_code=None)

@app.route('/generate', methods=['POST'])
def generate_qr():
    url = request.form['url']
    img = qrcode.make(url)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return render_template('index.html', qr_code=img_base64, url=url)

@app.route('/download', methods=['POST'])
def download_qr():
    url = request.form['url']
    img = qrcode.make(url)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='qr_code.png')

if __name__ == '__main__':
    app.run(debug=True)