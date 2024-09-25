'''modules needed for the python main file'''
from . import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    