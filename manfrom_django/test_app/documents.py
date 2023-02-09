from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

import main
from .models import Visitor


@registry.register_document
class VisitorDocument(Document):
    class Index:
        name = 'visitors'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Visitor
        fields = main.main()
