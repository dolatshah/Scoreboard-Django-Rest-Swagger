from rest_framework.decorators import api_view

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PlayerSerializer
from .models import Player

from rest_framework.exceptions import ValidationError, ParseError


class PlayerViewSet(viewsets.ModelViewSet):
	"""
    retrieve:
        Returns a list of all **active** players in the database. For more details on how players are created please see here [ref]. [ref]: http://localhost:8000/players

    list:
        Return all players, ordered by score.

    create:
        Create a new player.

    delete:
        Remove an existing player.

    partial_update:
        Update one or more fields on an existing player.
        http://localhost:8000/players/{id}

    update:
        Update a player.

    """
	queryset = Player.objects.all().order_by('points')
	serializer_class = PlayerSerializer

	def patch(self, request, pk):
		"""
		
		"""
		testmodel_object = self.get_object(pk)
		serializer = PlayerSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
		if serializer.is_valid(): #check if the serializer is valid
			serializer.save()
			return JsonResponse(code=201, data=serializer.data)
		return JsonResponse(code=400, data="wrong parameters")


@api_view(['POST'])
def pointsUpdate(request, pk):
	"""
	Update score of a player

	{
	    "action" : "plus"
	}

	or 

	{
	    "action" : "minus"
	}

	[ref]

	[ref]: http://localhost:8000/pointsUpdate/<id>/
    """
	player = Player.objects.get(id=pk)

	serializer = PlayerSerializer(instance=player)

	req = request.data
	
	# action can only be plus or minus
	if 'action' in req:
		if req['action'] == 'plus':
			player.points += 1
		if req['action'] == 'minus':
			player.points -= 1
		else:
			raise ValidationError
	else:
		return JsonResponse(code=400, data="wrong parameters")

	
	player.save()

	return Response(serializer.data)