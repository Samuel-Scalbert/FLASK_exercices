from flask import Flask
from app.app import version

app = Flask(__name__)
print(version)
app.run()
