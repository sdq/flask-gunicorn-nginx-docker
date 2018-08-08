from flask_script import Manager
from myapp import create_app

app = create_app()
manager = Manager(app)

# @manager.command
# def hello():
#     print "hello"

if __name__ == "__main__":
    manager.run()