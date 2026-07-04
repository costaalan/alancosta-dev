#!/opt/hermes/.venv/bin/python3
"""Servidor da página pessoal alancosta.dev"""
import os, sys
sys.path.insert(0, '/opt/data/.pymupdf_pkg')
from flask import Flask, send_from_directory

app = Flask(__name__)
SITE_DIR = '/opt/data/site-alancosta'

@app.route('/')
def index():
    return send_from_directory(SITE_DIR, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(SITE_DIR, path)

if __name__ == '__main__':
    print("🌐 alancosta.dev rodando em http://0.0.0.0:9090")
    app.run(host='0.0.0.0', port=9090, debug=False)
