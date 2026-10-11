from django import models

class Entity( models.Model ):
    hp = models.IntegerField( default=100 )
    armory =  models.IntegerField( blank=True )
    Name = models.CharField( blank=True, max_lenght=20)

   