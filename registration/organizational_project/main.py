'''modules needed for the python main file'''
try:
    from organizational_project import create_app
except ImportError:
    from . import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    