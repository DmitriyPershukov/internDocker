

from django.http import HttpResponse
from django.views.generic import ListView

import vocabulary.models, vocabulary.customserializers
import vocabulary.customserializers
from django.views import View
from django.apps import apps
from django.utils.module_loading import import_string
from django.utils.decorators import decorator_from_middleware, decorator_from_middleware_with_args

from django.utils.decorators import method_decorator
from middleware import APISecretMiddleware


argsmiddleware = decorator_from_middleware_with_args(APISecretMiddleware)


class APIViewMixin(View):
    apiMiddleware = decorator_from_middleware(APISecretMiddleware)
    @method_decorator(APISecretMiddleware)
    def dispatch(self, *args, **kwargs):
        return super().dispatch( *args, **kwargs)

class CategoriesView(APIViewMixin, View):

    def get(self, request, *args, **kwargs):
        serializer = vocabulary.customserializers.CategorySerialiser();b

        return HttpResponse(serializer.serialize(vocabulary.models.Categories.objects.all()),content_type='application/json')

class ThemesView(APIViewMixin, View):
    def get(self, request, id= None, *args, **kwargs):
        if (id!= None):
            serializer = vocabulary.customserializers.ThemesSerialiser(showWords=True);
            return HttpResponse(serializer.serialize([vocabulary.models.Theme.objects.get(pk= id)]), content_type='application/json')
        else:
            serializers = vocabulary.customserializers.ThemesSerialiser(showWords=False);
            return HttpResponse(serializers.serialize(vocabulary.models.Theme.objects.all()), content_type='application/json',)

class LevelsView(APIViewMixin,View):
    def get(self, request, *args, **kwargs):
        serializers = vocabulary.customserializers.LevelsSerialiser();
        responce = HttpResponse();
        responce.write(serializers.serialize(vocabulary.models.Level.objects.all()))
        return HttpResponse(serializers.serialize(vocabulary.models.Level.objects.all()), content_type='application/json');

class WordView(APIViewMixin,View):

    def get(self,request, id,*args, **kwargs):
        serializers=vocabulary.customserializers.WordSerialiser()
        return HttpResponse(serializers.serialize([vocabulary.models.Word.objects.get(pk=id)]), content_type='application/json')