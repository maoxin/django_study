from django.db import models

class Star(models.Model):
    star_name = models.CharField(max_length=200)
    star_distance = models.BigIntegerField()
    star_color = models.CharField(max_length=200)

    def __unicode__(self):
        return u'name: %s; distance: %d; color: %s ;' % (self.star_name, self.star_distance, self.star_color)