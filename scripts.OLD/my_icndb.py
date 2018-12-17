#!/usr/bin/env python3

"""
GET
/joke - return all jokes
/joke/<id> - returns a specific joke
/joke/random - returns a random joke
/joke/random/<n> - returns n random jokes

POST
/joke - add a joke to the database

PUT
/joke/<id> - update joke at id

DELETE
/joke/<id> - delete joke with specified id
"""

import uuid
import random
from bottle import run, get, post, put, delete, request

jokes_dict = { "jokes": {
    "1": 'Chuck Norris is a real badass and this is hilarious.',
    "2": 'Chuck Norris is either dead or my watch has stopped.',
    "3": 'No soup for you!!!!!!!!1``1`1111',
    }
}

#@get('/aaron')
#def aaron():
#    one_time_key = str(uuid.uuid4())
#    response.set_cookie('secret_key', one_time_key)
#    insert_into_valid_uuid_list(one_time_key)
#    return '<a href="/' + one_time_key + '">http://localhost/aaron/' + one_time_key + '</a>'
#
#@get('/aaron/<key>')
#def secret_key_page(key):
#    if key_valid(key):
#        add_to_blacklist(key)
#        result = secret_gen()
#    else:
#        return 404
#    return

@get('/joke')
def return_all_jokes():
    return jokes_dict

@get('/joke/<id>')
def return_specific_joke(id):
    try:
        return jokes_dict['jokes'][id]
    except:
        return 404

@get('/joke/random')
def return_random_joke():
    return jokes_dict['jokes'][random.choice(list(jokes_dict['jokes'].keys()))]

@get('/joke/random/<n:int>')
def return_random_jokes(n):
    if n > len(jokes_dict['jokes']):
        n = 1
    to_return = []
    for _ in range(n):
        to_return.append(jokes_dict['jokes'][random.choice(list(jokes_dict['jokes'].keys()))])

    return '<br />'.join(to_return)

@post('/joke')
def add_new_joke():
    njokes = len(jokes_dict['jokes'])
    jokes_dict['jokes'][str(njokes + 1)] = request.params.joke
    return 'Sucessfully added your joke!'

@put('/joke/<id>')
def update_joke(id):
    try:
        jokes_dict['jokes'][id] = request.params.joke
    except:
        return 'Joke ID not found!'

@delete('/joke/<id>')
def delete_joke(id):
    try:
        del jokes_dict['jokes'][id]
    except:
        return 'Joke ID not found!'

run(hostname='localhost', port=9999)
