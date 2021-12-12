from flask import Flask
app = Flask(__name__)

count = 0

@app.route('/')
def main():
    global count
    count += 1
    return 'I have been viewed ' + str(count) + ' times.'
