from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
        <head>
            <title>Docker Flask App</title>
        </head>
        <body>
            <h1>Welcome to the Docker Flask App</h1>
            <form action="/greet" method="POST">
                Enter your name: <input type="text" name="username">
                <input type="submit" value="Submit">
            </form>
            <p><a href="/about">About this App</a></p>
        </body>
        </html>
    '''

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        user_input = request.form.get('username', '').strip()
        if not user_input:
            return "Error: Name cannot be empty. Please go back and enter your name."
        return f"""Hello {user_input}, Welcome to this app for Docker demonstration. 
        Please consider liking and subscribing to the channel.
        
        <p><a href="/about"> About this App </a></p>
        
        """
    else:
        return redirect(url_for('index'))

@app.route('/about')
def about():
    return '''
        <html>
        <head>
            <title>About</title>
        </head>
        <body>
            <h1>About this App</h1>
            <p>This is a simple Flask application designed to demonstrate Docker integration.</p>
            <p>It includes basic features like user input, routing, and error handling.</p>
            <p><a href="/">Go back to Home</a></p>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)