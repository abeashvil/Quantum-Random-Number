from flask import Flask, render_template, jsonify
import rand_generator

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for generating a random number (to be called by the popup)
@app.route('/generate-random-number')
def generate_random_number():
    return jsonify(number=rand_generator.generate_rand())

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

