from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_github_stats(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        user_data = get_github_stats(username)

        if user_data:
            return render_template('index.html', user_data=user_data)
        else:
            return render_template('index.html', error='User not found.')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

