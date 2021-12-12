from flask import Flask
app = Flask(__name__)

file = open('cuvar.txt', 'r')
count = int(file.read())
file.close()

@app.route('/')
def main():
    global count
    count += 1
    
    file = open('cuvar.txt', 'w+')
    file.write(str(count))
    file.close()

    return 'I have been viewed ' + str(count) + '. times.'



