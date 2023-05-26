from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from shop.models import Car


@registry.register_document
class CarDocument(Document):
    class Index:
        name = 'cars'

    class Django:
        model = Car
        fields = [
            'id',
            'name',
            'num_cylinders',
            'num_seats',
            'color',
            'engine_capacity',
        ]