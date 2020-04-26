import logging

import azure.functions as func

from . import run

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP Request received')

    params = req.params.get('params')
    
    if not params:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            params = req_body.get('params')

    if params:
        resp = run.run(params)
        return func.HttpResponse(resp)
    else:
        return func.HttpResponse(
             "params missing in request",
             status_code=200
        )
