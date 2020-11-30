from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Player

class AccountTests(APITestCase):
	def test_create_player(self):
		"""
		Ensure we can create a new player object.
		"""
		data = {
			"name": "test",
			"address": "test",
			"points": 0,
			"age": 1
		}
		response = self.client.post('/players/', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Player.objects.count(), 1)
		self.assertEqual(Player.objects.get().name, 'test')

	def test_delete_player(self):
		"""
		Ensure we can delete a new player object.
		"""
		data = {
			"name": "test2",
			"address": "test2",
			"points": 2,
			"age": 2
		}
		response = self.client.post('/players/', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Player.objects.count(), 1)
		self.assertEqual(Player.objects.get().name, 'test2')

		# once created we delete it and check the count

		id = Player.objects.get().id
		response = self.client.delete('/players/'+str(id)+'/', data, format='json')
		self.assertEqual(response.status_code, 204)
		self.assertEqual(Player.objects.count(), 0)


	def test_update_player_plus(self):
		"""
		Ensure we can update a new player object.
		"""
		data = {
			"name": "test2",
			"address": "test2",
			"points": 3,
			"age": 2
		}
		response = self.client.post('/players/', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Player.objects.count(), 1)
		self.assertEqual(Player.objects.get().name, 'test2')

		# once created we update the score

		data = {
			'action' : 'plus'
		}
		id = Player.objects.get().id
		response = self.client.post('/pointsUpdate/'+str(id)+'/', data, format='json')
		self.assertEqual(Player.objects.count(), 1)
		self.assertEqual(Player.objects.get().points, 4)

	def test_update_player_plus(self):
		"""
		Ensure we can update a new player object.
		"""
		data = {
			"name": "test2",
			"address": "test2",
			"points": 3,
			"age": 2
		}
		response = self.client.post('/players/', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Player.objects.count(), 1)
		self.assertEqual(Player.objects.get().name, 'test2')

		# once created we update the score

		data = {
			'action' : 'minus'
		}
		id = Player.objects.get().id
		response = self.client.post('/pointsUpdate/'+str(id)+'/', data, format='json')
		self.assertEqual(Player.objects.count(), 1)
		self.assertEqual(Player.objects.get().points, 2)

	def test_update_player_wrong(self):
		"""
		Ensure about the error handling.
		"""
		data = {
			"name": "test2",
			"address": "test2",
			"points": 3,
			"age": 2
		}
		response = self.client.post('/players/', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Player.objects.count(), 1)
		self.assertEqual(Player.objects.get().name, 'test2')

		# sending a wrong parameter
		
		data = {
			'action' : 'add'
		}
		id = Player.objects.get().id
		response = self.client.post('/pointsUpdate/'+str(id)+'/', data, format='json')
		self.assertEqual(Player.objects.count(), 1)
		self.assertEqual(Player.objects.get().points, 3)
		self.assertEqual(response.status_code, 400)
