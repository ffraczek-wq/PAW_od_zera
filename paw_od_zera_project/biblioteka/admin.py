from django.contrib import admin

# Register your models here.

from .models import Genre, Author, Book

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)

class OsobaAdmin(admin.ModelAdmin):
    # zmienna list_display przechowuje listę pól, które mają się wyświetlać w widoku listy danego modelu w panelu administracynym
    list_display = ["imie" , "nazwisko" , "stanowisko"]

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Osoba, OsobaAdmin)

class OsobaAdmin(admin.ModelAdmin):
    list_display = ["imie" , "nazwisko" , "stanowisko"]
    list_filter = ["stanowisko" , "data_dodania"]