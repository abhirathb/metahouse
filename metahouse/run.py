import logging
from . import interfaces
import json 
funcs = [ interfaces.nnacres ]
def run(params):
    responses = []
    for func in funcs:
        responses.append(func.search(params))
    response_json = json.dumps(responses)
    return response_json