from rest_framework.serializers import ModelSerializer
from main import main
from test_app.models import Visitor


class VisitorSerializer(ModelSerializer):
    class Meta:
        model = Visitor
        fields = main()
