
# Register your models here.
from django.contrib import admin

# Register your models here.

import vocabulary.models as mod


class WordInline(admin.StackedInline):
    model = mod.Word
    extra = 0

class ThemeAdmin(admin.ModelAdmin):
    inlines = [WordInline]
    #list_display = ('avatar_tag','user')  # As a field, specify the method that will return the picture tag in the list of user profiles.
    readonly_fields = ['photo_tag']

admin.site.register(mod.Theme, ThemeAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ['icon_tag']

class WordAdmin(admin.ModelAdmin):
    readonly_fields = ['pronunciation_tag']
admin.site.register(mod.Categories, CategoriesAdmin)
admin.site.register(mod.Word, WordAdmin)

admin.site.register(mod.Level)