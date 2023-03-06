from flask import Flask, render_template, jsonify

#importing functionality from flask and putting it into variable app.
app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Bengaluru, India',
    'salary': 'Rs. 1,00,000'
  },
  {
    'id': 2,
    'title': 'software engineer',
    'Location': 'delhi, India',
    'salary': 'Rs. 2,00,000'
  },
  {
    'id': 3,
    'title': 'front-end developer',
    'Location': 'kolkata, India',
  },
  {
    'id': 4,
    'title': 'backend developer',
    'Location': 'hyderabad, India',
    'salary': 'Rs. 4,00,000'
  },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Jovian")


@app.route('/jobs')
def find_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
