from django_twilio.decorators import twilio_view
from twilio.twiml import Response
import requests
import json


def query_pokeapi(resource_uri):
    '''
    Query PokeAPI and return a Python dictionary of the HTTP response body.
    Returns None if a query error occurs
    '''
    url = 'http://pokeapi.co{0}'.format(resource_uri)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    return None


def gather_pokemon_data(pokemon_data):
    '''
    Gather description and sprite data for TwiML response
    '''
    # Gather resource uri based on pokemon data
    description_resource_uri = pokemon_data['descriptions'][0]['resource_uri']
    sprite_resource_uri = pokemon_data['sprites'][0]['resource_uri']

    # Query PokeAPI for new data
    description_data = query_pokeapi(description_resource_uri)
    sprite_data = query_pokeapi(sprite_resource_uri)

    pokemon_image = 'http://pokeapi.co{0}'.format(sprite_data['image'])
    description = description_data['description']

    return (pokemon_image, description)


def compose_message_response(pokemon_data):
    '''
    Compose the appropriate Twilio response based on the Pokemon data
    '''

    pokemon_image, description = gather_pokemon_data(pokemon_data)

    # Format TwiML response
    twiml = Response()
    twiml.message(description).media(pokemon_image)
    return twiml

@twilio_view
def incoming_message(request):
    '''
    The Django view endpoint for inbound Twilio SMS messages
    '''
    body = request.POST.get('Body', '')
    twiml = Response()
    twiml.message('Hello twilio')
    return twiml
