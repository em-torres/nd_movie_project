from movies_gallery import app


@app.route('/')
def index():
    return 'Hello World!'
