from django.contrib import admin
from home.models import Author, Book, Genre
# Register your models here.


#admin.site.register(Book)
#admin.site.register(Genre)
#admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=('id','name')
    list_filters=('name',' purchase_ data',('author',admin.RelatedOnlyFieldListFilter))

    list_filter=('name','purchase_date','author')
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass   

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass