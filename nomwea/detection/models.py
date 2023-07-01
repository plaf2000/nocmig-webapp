# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Codes(models.Model):
    species = models.ForeignKey('Species', models.DO_NOTHING, blank=True, null=True)
    non_bird = models.ForeignKey('NonBird', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codes'


class NonBird(models.Model):
    it = models.CharField(max_length=255, blank=True, null=True)
    de = models.CharField(max_length=255, blank=True, null=True)
    fr = models.CharField(max_length=255, blank=True, null=True)
    es = models.CharField(max_length=255, blank=True, null=True)
    pt = models.CharField(max_length=255, blank=True, null=True)
    en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'non_bird'


class Species(models.Model):
    lat = models.CharField(max_length=255, blank=True, null=True)
    it = models.CharField(max_length=255, blank=True, null=True)
    de = models.CharField(max_length=255, blank=True, null=True)
    fr = models.CharField(max_length=255, blank=True, null=True)
    es = models.CharField(max_length=255, blank=True, null=True)
    pt = models.CharField(max_length=255, blank=True, null=True)
    en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'species'
