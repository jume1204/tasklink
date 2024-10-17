from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/task')
def task():
    return render_template('task.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Aquí puedes agregar la lógica para validar las credenciales
        # y redirigir al usuario si las credenciales son correctas.
        return redirect(url_for('index'))  # Redirigir a la página principal tras iniciar sesión.
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
