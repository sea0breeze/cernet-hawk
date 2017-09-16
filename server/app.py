
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session, flash

app = Flask(__name__)

app.secret_key = 'sLdSPRk4OjrYkP2r8OIvhMGfTxL0mdAH'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7682, debug=True)
