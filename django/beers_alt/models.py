from django.db import models

# class Bar(models.Model):
#     name = models.CharField(max_length=20, primary_key=True)
#     address = models.CharField(max_length=20, blank=True)

class Drinker(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    address = models.CharField(max_length=20, blank=True)

# class Frequents(models.Model):
#     drinker = models.ForeignKey(Drinker, db_column='drinker')
#     bar = models.ForeignKey(Bar, db_column='bar')
#     times_a_week = models.SmallIntegerField(null=True, blank=True)
#
# class Beer(models.Model):
#     name = models.CharField(max_length=20, primary_key=True)
#     brewer = models.CharField(max_length=20, blank=True)
#
# class Serves(models.Model):
#     bar = models.ForeignKey(Bar, db_column='bar')
#     beer = models.ForeignKey(Beer, db_column='beer')
#     price = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
#
# class Likes(models.Model):
#     drinker = models.ForeignKey(Drinker, db_column='drinker')
#     beer = models.ForeignKey(Beer, db_column='beer')
