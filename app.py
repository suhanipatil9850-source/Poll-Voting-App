from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store votes
votes = {
    "Option A": 0,
    "Option B": 0,
    "Option C": 0
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    option = request.form.get('option')
    if option in votes:
        votes[option] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html', votes=votes)

if __name__ == '__main__':
    app.run(debug=True)
