# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WeatherMeasurement(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    remote_id = models.BigIntegerField(db_column='REMOTE_ID', blank=True, null=True)  # Field name made lowercase.
    ambient_temperature = models.DecimalField(db_column='AMBIENT_TEMPERATURE', max_digits=6, decimal_places=2)  # Field name made lowercase.
    air_pressure = models.DecimalField(db_column='AIR_PRESSURE', max_digits=6, decimal_places=2)  # Field name made lowercase.
    humidity = models.DecimalField(db_column='HUMIDITY', max_digits=6, decimal_places=2)  # Field name made lowercase.
    wind_direction = models.DecimalField(db_column='WIND_DIRECTION', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    direction_variance = models.DecimalField(db_column='DIRECTION_VARIANCE', max_digits=3, decimal_places=3)  # Field name made lowercase.
    wind_speed = models.DecimalField(db_column='WIND_SPEED', max_digits=6, decimal_places=2)  # Field name made lowercase.
    wind_gust_speed = models.DecimalField(db_column='WIND_GUST_SPEED', max_digits=6, decimal_places=2)  # Field name made lowercase.
    rainfall = models.DecimalField(db_column='RAINFALL', max_digits=6, decimal_places=2)  # Field name made lowercase.
    cpu_temp = models.DecimalField(db_column='CPU_TEMP', max_digits=6, decimal_places=1)  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WEATHER_MEASUREMENT'
