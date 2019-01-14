from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Choice, Question, Person, SalesReport

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),      
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]    
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# This is the old way
admin.site.register(Question, QuestionAdmin)

# This is the new way, which includes Import and Export Options
@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(SalesReport)
class SalesReportAdmin(ImportExportModelAdmin):
    pass


"""
@admin.register(Inventory)
class InventoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Airline)
class AirlineAdmin(ImportExportModelAdmin):
    pass

@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    pass

@admin.register(Route)
class RouteAdmin(ImportExportModelAdmin):
    pass
"""
