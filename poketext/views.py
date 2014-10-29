from django_twilio.views import twilio_view
from twilio.twiml import Response
import requests
import json

BASE_URL = 'http://pokeapi.co'

def query_pokeapi(resource_uri):
    url = '{0}{1}'.format(BASE_URL, resource_uri)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    return None


@twilio_view
def incoming_message(request):

    twiml = Response()

    body = request.POST.get('Body', '')
    body = body.lower()

    pokemon_url = '/api/v1/pokemon/{0}/'.format(body)
    pokemon = query_pokeapi(pokemon_url)

    if pokemon:
        sprite_uri = pokemon['sprites'][0]['resource_uri']
        description_uri = pokemon['descriptions'][0]['resource_uri']

        sprite = query_pokeapi(sprite_uri)
        description = query_pokeapi(description_uri)

        message = '{0}, {1}'.format(pokemon['name'], description['description'])
        image = '{0}{1}'.format(BASE_URL, sprite['image'])

        frm = request.POST.get('From', '')
        if '+44' in frm:
            twiml.message('{0} {1}'.format(message, image))
            return twiml
        twiml.message(message).media(image)
        return twiml

    twiml.message("Something went wrong! Try 'Pikachu' or 'Rotom'")
    return twiml
