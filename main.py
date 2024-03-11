import hug
import falcon
import card_search

"""Add middleware to response and request"""
@hug.request_middleware()
def process_data(request, response):
    request.env['SERVER_NAME'] = 'changed'

@hug.response_middleware()
def process_data(request, response, resource):
    response.set_header('MyHeader', 'Value')

@hug.get('/happy_birthday')
def happy_birthday(name, age:hug.types.number=1):
  """Say Happy birthday"""
  return "Happy {age} Birthday {name}!".format(**locals())

"""Versioning with hug"""
@hug.get('/echo', versions=1)
def echo(text):
    return text


@hug.get('/echo', versions=range(2, 5))
def echo(text):
    return "Echo: {text}".format(**locals())

@hug.get('/hello_there')
def hello_there(name):
  return "general {}".format(name)

@hug.post('/add_cards_to_db')
def add_cards_to_db(body,response):
  print("GOT {}: {}".format(type(body), repr(body)))
  try:
    name = body.get('name')
    nameType = body.get('nameType')
  except Exception as error:
    response.status = falcon.HTTP_400
    return {'error': 'somehting went wrong'}
  if(name==None or nameType == None):
    response.status = falcon.HTTP_400
    return {'error': 'unable to parse json in handler'}
  card_info = card_search.search_by_name_exact(name)
  return card_info
  # if (!name || !nameType):
  #   response.status = falcon.HTTP_400
  #   return {'error': 'unable to parse json in handler'}
