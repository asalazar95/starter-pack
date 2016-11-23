#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    server.py
    ~~~~~~~~~

    Python application built using Flask.
"""

from flask import Flask, render_template


app = Flask(__name__, template_folder='frontend', static_url_path='', static_folder='')


@app.route('/')
def index():
    """Render the initial view."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)