from hello_world.formater import SUPPORTED, PLAIN
from flask import request

moje_imie = "Kamil"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
@@ -14,6 +15,7 @@ def index():
    return get_formatted(msg, moje_imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)