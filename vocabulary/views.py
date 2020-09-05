

from django.http import HttpResponse
import vocabulary.models, vocabulary.customserializers
import vocabulary.customserializers
from django.views import View
from django.apps import apps
from django.utils.module_loading import import_string

class CategoriesView(View):
    def get(self, request, *args, **kwargs):
        serializer = vocabulary.customserializers.CategoriesSerialiser();
        return HttpResponse(serializer.serialize(vocabulary.models.Categories.objects.all()), content_type='application/json')
class ThemesView(View):
    def get(self, request, id = None, *args, **kwargs):

        if (id!= None):
            serializer = vocabulary.customserializers.ThemesSerialiser(showWords=True);
            return HttpResponse(serializer.serialize([vocabulary.models.Theme.objects.get(pk= id)]), content_type='application/json')
        else:
            serializers = vocabulary.customserializers.ThemesSerialiser(showWords=False);
            return HttpResponse(serializers.serialize(vocabulary.models.Theme.objects.all()), content_type='application/json',)

class LevelsView(View):
    def get(self, request, *args, **kwargs):

        serializers = vocabulary.customserializers.LevelsSerialiser();
        responce = HttpResponse();
        responce.write(serializers.serialize(vocabulary.models.Level.objects.all()))
        return HttpResponse(serializers.serialize(vocabulary.models.Level.objects.all()),content_type='application/json');

class WordView(View):
    def get(self, request, id, *args, **kwargs):
        serializers=vocabulary.customserializers.WordSerialiser()
        return HttpResponse(serializers.serialize([vocabulary.models.Word.objects.get(pk=id)]), content_type='application/json')

class AdminView(View):
    def _setup(self):
        AdminSiteClass = import_string(apps.get_app_config('admin').default_site)
        self._wrapped = AdminSiteClass()