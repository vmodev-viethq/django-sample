from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from polls.models import Poll
from polls.serializers import PollSerializer, PollCreateBodySerializer

# Create your views here.


class PollViewSet(viewsets.ViewSet):
    serializer_class = PollSerializer

    def list(self, request):
        queryset = Poll.objects.all()
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Poll.objects.all()
        poll = get_object_or_404(queryset, pk=pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    @extend_schema(request=PollCreateBodySerializer)
    def create(self, request):
        serializer = PollCreateBodySerializer(data=request.data)
        serializer.is_valid()
        instance = serializer.save()
        response = PollSerializer(instance).data
        return Response(response)

    def update(self, request):
        serializer = PollSerializer(data=request.data)
        serializer.is_valid()
        instance = serializer.save()
        response = PollSerializer(instance).data
        return Response(response)

    def destroy(self, request, pk=None):
        deleted = Poll.objects.filter(id=pk).delete()
        msg = "Delete successfully" if deleted[0] == 1 else "Delete failed"
        return Response({"msg": msg})
