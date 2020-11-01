
from .models import Course
from .serializer import CourseSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    # list, create, retrieve, update, partial_update, destroy
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 


    # add our own path "newset"
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('id').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)