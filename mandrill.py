import requests
import json
from bson import json_util
from settings import MANDRILL_APIKEY, MANDRILL_ENDPOINT

def send_with_template(form, contents):
    form_fields = ["to"] #['subject', 'from_email', 'from_name', 'to']
    message = { k:form.get(k, None) for k in form_fields }
    message.update(
            {'global_merge_vars': [{ 'name':"f_"+key, 'content':value[0]} for key, value in contents.iteritems() if value[0]]}
        )
    data = {
            'key': MANDRILL_APIKEY,
            'template_name': form.get('mandrill_template', form['name']),
            'template_content' :[],
            'message': message
        }

    print "Sending"
    print data

    response = requests.post(
            MANDRILL_ENDPOINT+"messages/send-template.json",
            data=json.dumps(data, default=json_util.default)
        )
    print response
    return response.json()
