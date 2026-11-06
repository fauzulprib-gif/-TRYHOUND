import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>TRYHOUND</title>
    <style>
    body{background:#111;color:white;font-family:sans-serif;text-align:center;padding-top:100px}
    h1{font-size:50px;color:#00ff88}
    .box{background:#222;padding:20px;border-radius:15px;display:inline-block}
    </style></head>
    <body>
    <h1>TRYHOUND</h1>
    <div class="box">
    <h2>Dashboard Zul Berhasil Online!</h2>
    <p>Web lu udah jalan di Render</p>
    <p>Status: AKTIF</p>
    </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
