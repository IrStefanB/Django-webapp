from django.db import models
from django.utils import timezone
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

# Create your models here.

class Catalog(models.Model):
    catalog_name = models.CharField(max_length=120, blank=False)
    catalog_type = models.CharField(max_length=120)
    catalog_timestamp = models.DateTimeField(auto_now_add=True)
    catalog_updated = models.DateTimeField(auto_now=True)
    catalog_date_field = models.DateTimeField(auto_now=False, auto_now_add=False)
    """instead of showing 'catalog object' as the name of the catalog ,
        it will use the catalog_name key for that"""
    def __str__(self):
        return self.catalog_name



class ExampleModel(DjangoCassandraModel):
     example_id   = columns.UUID(primary_key=True, default=uuid.uuid4)
     example_type = columns.Integer(index=True)
     created_at   = columns.DateTime.truncate_microseconds
     description  = columns.Text(required=False)

     def __str__(self):
        return self.description