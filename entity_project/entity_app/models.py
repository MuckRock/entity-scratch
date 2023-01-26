from django.db import models


class Entity(models.Model):
    ACCESS_CHOICES = [("Public", 0), ("Private", 1)]

    name = models.CharField(max_length=500)
    wikidata_id = models.CharField(max_length=16, editable=False)
    owner = models.ForeignKey(
        "auth.User", related_name="entities", on_delete=models.CASCADE
    )
    description = models.TextField(
        default="A description of this entity that will be replaced."
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    access = models.CharField(max_length=20, choices=ACCESS_CHOICES, default="Public")

    def save(self, *args, **kwargs):
        # TODO: Transformations
        super().save(*args, **kwargs)
