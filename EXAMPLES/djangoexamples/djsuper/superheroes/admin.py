from django.contrib import admin

# Register your models here.

from superheroes.models import Superhero, Power, Enemy, City # <1>

class SuperheroAdmin(admin.ModelAdmin):
    search_fields = ['name', 'real_name', 'secret_identity']
    empty_value_display = '**NADA**'

admin.site.register(Superhero, SuperheroAdmin)  # <2>
admin.site.register(City) # <2>
admin.site.register(Enemy) # <2>

class PowerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']


admin.site.register(Power, PowerAdmin) # <2>

