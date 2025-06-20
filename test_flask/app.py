from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Simple in-memory list to store attendance (resets every restart!)
attendance = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        attendance.append({'name': name, 'time': timestamp})
        return redirect(url_for('home'))
    return render_template('index.html', attendance=attendance)

if __name__ == '__main__':
    app.run(debug=True)
