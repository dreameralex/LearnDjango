# Your first Django Sites
# Django ORM 
## Fixtures
Show the JASO format
```shell
python manage.py dumpdata bands | python -m json.tool
```

```shell
python manage.py dumpdata bands > bands.json
python manage.py loaddata bands
```
## Danger zone, or know thy SQL

# Django Admin
## Touring the Django Admin
Django divides users into three classes:
- General users
- Staff
- Admins
### Creating an admin user
```sh
python manage.py createsuperuser

```
admin
admin@example.com
000000

### Adding your own models
admin.py file is where you declare that you want a Model to participate
in the Django Admin.

The `register() `function can also be used as a class decorator. This is my preference,
as it keeps the registration close to the admin.ModelAdmin class declaration.
Each registered admin.ModelAdmin class gets a set of CRUD pages.

```python
from django.contrib import admin  
from bands.models import Musician 
"""
Use the register() function as a class decorator to associate the admin class with the model.
"""
@admin.register(Musician)  
# Inherit admin.ModelAdmin.
class MusicianAdmin(admin.ModelAdmin):  
    pass
```

## Customizing a listing page
By default, each object gets represented using the class’s `.__str__()` method. You can change this behavior by adding the `list_display` attribute to the` admin.ModelAdmin class`, which controls which columns are shown on the listing page.

```python
from django.contrib import admin  
from bands.models import Musician  
@admin.register(Musician)  
class MusicianAdmin(admin.ModelAdmin):  
    list_display = ('id', 'last_name', 'show_weekday')  
  
    def show_weekday(self, obj):  
        # Fetch weekday of artist’s birth  
        return obj.birth.strftime("%A")  
    show_weekday.short_description = "Birth Weekday"
```

### Sorting and searching
```python 
class MusicianAdmin(admin.ModelAdmin):  
    ......
    search_fields = ("last_name", "first_name",)
```
### Filtering


















