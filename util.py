from bson import json_util
import json
from flask import current_app, request

def jsonify(*args, **kwargs):
    return current_app.response_class(
            json.dumps(
                    dict(*args, **kwargs),
                    indent=None if request.is_xhr else 2,
                    default=json_util.default
                ), 
            mimetype='application/json'
        )