from flask import Flask, jsonify

app = Flask(__name__)

# Route 1: Home Page
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Route 2: About Page
@app.route('/about')
def about():
    return "This is the About Page. Learn more about us here."

# Route 3: Contact Page
@app.route('/contact')
def contact():
    return jsonify({
        "email": "contact@example.com",
        "phone": "+123-456-7890"
    })

if __name__ == '__main__':
    app.run(debug=True)
