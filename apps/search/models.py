from django.db import models
from elasticsearch_dsl import Document, Text, Date, Keyword

class SearchDocument(Document):
    title = Text()
    content = Text()
    tenant_id = Keyword()
    created_at = Date()

    class Index:
        name = 'tenant_search'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    def save(self, **kwargs):
        from django_tenants.utils import get_current_schema_name
        self.tenant_id = get_current_schema_name()
        return super().save(**kwargs)
