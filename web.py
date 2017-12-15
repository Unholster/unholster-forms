# -*- coding: utf-8 -*-
# import accounts
from raven.contrib.flask import Sentry
from flask import Flask, request, redirect, abort
import ses
import urlparse
# from util import jsonify

app = Flask(__name__)
sentry = Sentry()
sentry.init_app(app)


@app.route('/')
def hello():
    return 'Hello World!\n'


@app.route('/submit', methods=["GET", "POST"])
def submit():
    data = dict(request.form)
    try:
        referer = request.referrer
        # form_name = data.pop("forms:form")[0]
        # account_name = data.pop("forms:account")[0]
        # redirect_path = data.pop("forms:redirect")[0]
    except KeyError:
        abort(403)

    attachments = [file for name, file in request.files.iteritems() if file]

    # account = accounts.find_one({"name": account_name})

    # if account is None:
    #     print("Account not found")
    #     abort(404)

    # form = account.form(form_name)
    # if form is None:
    #     print("Form not found %s" % form_name)
    #     abort(404)

    # if not form.referer_allowed(referer):
    #     print("Referer not allowed %s" % referer)
    #     abort(404)

    form = UnholsterForm(data)
    # result = ses.send_with_template(form, data, attachments)
    ses.send(form.recipients, form.subject, form.content, attachments)
    # print(result)
    # account.submits().insert({'form': form['_id'], 'data': data, 'mandrill_result': esult})

    if form.redirect_url:
        redirect_url = urlparse.urljoin(referer, form.redirect_url[0])
        return redirect(redirect_url)
    else:
        return 'Sent'


# @app.route('/account/<account_name>')
# def account(account_name):
#     account = accounts.find_one({"name": account_name})
#     return jsonify(
#         account=account,
#         submits=list(account.submits().find())
#     )


class UnholsterForm:
    def __init__(self, data):
        self.recipients = ['contacto@unholster.com']
        self.subject = u'Contacto: {subject[0]}'.format(**data)
        self.content = self._content(data)
        self.redirect_url = data.get('redirect_url')

    def _content(self, data):
        tmpl = (
            u"Nombre: {name[0]} <br/>"
            u"E-mail: <a href=mailto:{email[0]}>{email[0]}</a> </br>"
            u"<pre>{message[0]}</pre>"
        )
        return tmpl.format(**data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
