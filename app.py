from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
    return 'Jay_Bots'


if name == "main":
    app.run()
