# example_webserver.py #
########################

from flask import Flask, request

import praw

app = Flask(__name__)

CLIENT_ID = 'FJT8Xw6bluRwsg'
CLIENT_SECRET = 'SEpjNE4ynxRw9Uf7JwSIduiPiuI'
REDIRECT_URI = r'http://127.0.0.1:65010/authorize_callback'

@app.route('/')
def homepage():
    #link_no_refresh = r.get_authorize_url('UniqueKey')
    #link_refresh = r.get_authorize_url('DifferentUniqueKey',
    #                                   refreshable=True)
    #link_no_refresh = "<a href=%s>link</a>" % link_no_refresh
    #link_refresh = "<a href=%s>link</a>" % link_refresh
    text = "First link. Not refreshable %s</br></br>" #% link_no_refresh
    text += "Second link. Refreshable %s</br></br>" #% link_refresh
    return text

@app.route('/authorize_callback')
def authorized():
    state = request.args.get('state', '')
    code = request.args.get('code', '')
    info = r.get_access_information(code)
    user = r.get_me()
    variables_text = "State=%s, code=%s, info=%s." % (state, code,
                                                      str(info))
    text = 'You are %s and have %u link karma.' % (user.name,
                                                   user.link_karma)
    back_link = "<a href='/'>Try again</a>"
    return variables_text + '</br></br>' + text + '</br></br>' + back_link

if __name__ == '__main__':
    r = praw.Reddit(user_agent='decuran',
                     client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET)
    # r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    app.run(debug=True, port=65010)