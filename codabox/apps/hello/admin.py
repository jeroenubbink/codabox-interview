from django.contrib import admin

from .models import Greet


class GreetAdmin(admin.ModelAdmin):
    model = Greet
    readonly_fields = ('id',)
    list_display = ('name', 'id',)


admin.site.register(Greet, GreetAdmin)
