from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users_list = [
    {'id': 1, 'name': 'John Doe', 'age': 28},
    {'id': 2, 'name': 'Jane Smith', 'age': 34},
    {'id': 3, 'name': 'Alice Brown', 'age': 22},
]


@app.route('/')
def home():
    return render_template('home.html', show_go_home_button=False)


@app.route('/about')
def about():
    return render_template('about.html', show_go_home_button=True)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html', show_go_home_button=True)


@app.route('/users')
def users():
    return render_template('users.html', users=users_list, show_go_home_button=True)


# Route for sending a message
@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        user_name = request.form['name']
        user_message = request.form['message']

        # Print the received message to the console
        print(f"Message from {user_name}: {user_message}")

        # Redirect to the users page after submitting the message
        return redirect(url_for('users'))


# Route for displaying a specific user's profile
@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = next((user for user in users_list if user['id'] == user_id), None)
    if user:
        return render_template('profile.html', user=user)
    return f'User with ID {user_id} not found.', 404


if __name__ == '__main__':
    app.run(debug=True)
