from django.contrib import admin
from .models import Social_links, Portfolio, Visitors, Portfolio_project, Info, Xabarlar

# Register your models here.
admin.site.register(Social_links)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = [ "name", "age", "jop"]
    search_fields = ["name", "age", "jop", "languages"]
    list_per_page = 10

admin.site.register(Visitors)

@admin.register(Portfolio_project)
class Protfolio_projectAdmin(admin.ModelAdmin):
    list_display = [ "title", "loyiha_url"]
    search_fields = ["title", "url"]
    list_per_page = 10

admin.site.register(Info)
admin.site.register(Xabarlar)