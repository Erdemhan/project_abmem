from ..main import resource_service as ResourceService
from django_model.db.models.models import Resource

def checkResources(resourceData: dict) -> [Resource]:
    return ResourceService.createFromData(resourceData)
