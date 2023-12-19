import sys
sys.path.append("D:/Projeler/abm/abmem_project/test")
from django.db import models
# TO USE DJANGO ORM


# BASE ENTİTY
class Base(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True ,null=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label= "db"
