from web_ui.bottle import route, run, template, static_file, get


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./')


@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)


@get('/login')  # or @route('/login')
def login():
    return '''
       This is a Message for ya
    '''


run(host='localhost', port=8080)
