from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Example route to handle form data (if you want to add a contact form)
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')
    # Process the form data (e.g., store it, send email, etc.)
    return redirect(url_for('home'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

