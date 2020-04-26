import logging
from . import interfaces

funcs = [ interfaces.nnacres ]
def run(params):
    for func in funcs:
        func.search(params)
    response_json = """
    { 'resp' : 'done' }
    """
    return response_json