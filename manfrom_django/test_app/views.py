import datetime

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from test_app.models import Visitor
from test_app.serializers import VisitorSerializer


class VisitorsView(ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


def visitor_page(request):

    return render(request, 'index.html', {'visitors': Visitor.objects.all()})


def visitor_app(request):
    return render(request, 'test_app.html')
