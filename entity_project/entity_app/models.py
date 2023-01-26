from django.db import models
from wikidata.client import Client


class Entity(models.Model):
    wikidata_client = None

    ACCESS_CHOICES = [("Public", 0), ("Private", 1)]

    name = models.CharField(max_length=500)
    wikidata_id = models.CharField(max_length=16)
    # It's not unheard of to have urls that are 2000 characters. https://stackoverflow.com/a/417184/87798
    wikipedia_url = models.CharField(max_length=2000)
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
        update_fields = kwargs.get("update_fields")
        if update_fields is not None and "wikidata_id" in update_fields:
            self.wikipedia_url = get_url_for_wikidata_id(self.wikidata_id)
            super().save(update_fields=["wikidata_id", "wikipedia_url"])

        super().save(*args, **kwargs)

    def get_url_for_wikidata_id(self, wikidata_id):
        if not self.wikidata_client:
            self.wikidata_client = Client()

        wd_entity = self.wikidata_client.get(wikidata_id, load=True)
        # TODO: Should there be a language property on the entity?
        # TODO: Use a library that gets this safely.
        return wd_entity.data["sitelinks"]["enwiki"]["url"]
