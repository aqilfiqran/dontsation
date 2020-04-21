from django.contrib import admin
from .models import DonateArticle, Donate
# Register your models here.


@admin.register(Donate)
class DonateAdmin(admin.ModelAdmin):
    list_display = ["name", 'email', 'donation', 'donateArticle',
                    'confirmation', 'barcode']


admin.site.register(DonateArticle)
