from django.test import TestCase, Client

from views import (
    query_pokeapi,
    incoming_message,
    gather_pokemon_data,
    compose_message_response
)


class TestPokeTextViews(TestCase):

    def setUp(self):
        self.pokemon_data = {
            'name': 'Pikachu',
            'descriptions': [
                {'resource_uri': '/api/v1/description/7/'}
            ],
            'sprites': [
                {'resource_uri': '/api/v1/sprite/2/'}
            ]
        }

        self.client = Client()

    def test_query_pokeapi_fails(self):
        fail_query = '/api/v1/pokemon/error/'
        result = query_pokeapi(fail_query)
        self.assertIsNone(result)

    def test_query_pokeapi_success(self):
        query = '/api/v1/pokemon/mew/'
        result = query_pokeapi(query)
        self.assertIsNotNone(result)
        self.assertEquals(result['name'], 'Mew')

    def test_gather_pokemon_data(self):
        result1, result2 = gather_pokemon_data(self.pokemon_data)
        self.assertEquals(result1, 'http://pokeapi.co/media/img/1.png')
        self.assertIn('can be seen napping in bright sunlight', result2)

    def test_compose_message_response(self):
        result = compose_message_response(self.pokemon_data)
        self.assertIn('<Response>', result.toxml())
        self.assertIn(
            '<Media>http://pokeapi.co/media/img/1.png</Media',
            result.toxml()
        )

    def test_incoming_message_failure(self):
        data = {'Body': 'This will fail'}
        result = self.client.post('/incoming/message', data)
        self.assertIn('Something went wrong!', result.content)

    def test_incoming_message_success(self):
        data = {'Body': 'Pikachu'}
        result = self.client.post('/incoming/message', data)
        self.assertIn(
            '<Media>http://pokeapi.co/media/img/25.png',
            result.content
        )
        self.assertIn('Pikachu', result.content)

    def test_incoming_message_failure(self):
        data = {'Body': 'This will fail'}
        result = self.client.post('/incoming/sms', data)
        self.assertIn('Something went wrong!', result.content)

    def test_incoming_message_success(self):
        data = {'Body': 'Pikachu'}
        result = self.client.post('/incoming/sms', data)
        self.assertNotIn(
            '<Media>http://pokeapi.co/media/img/25.png',
            result.content
        )
        self.assertIn('Pikachu', result.content)
