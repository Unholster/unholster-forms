# -*- coding: utf-8 -*-
# import accounts
from flask import Flask, request, redirect, abort
import ses
import urlparse
# from util import jsonify
import base64

app = Flask(__name__)


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

    attachments = []
    for filename, f in request.files.iteritems():
        attachments.append({
            "type": f.content_type,
            "name": f.filename,
            "content": base64.b64encode(f.read()),
        })

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
        redirect_url = urlparse.urljoin(referer, form.redirect_url)
        return redirect(redirect_url)


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
        self.subject = 'Contacto vía sitio web'
        self.content = self._content(data)
        self.redirect_url = None

    def _content(self, data):
        tmpl = """
        """
        return tmpl.format(**data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
