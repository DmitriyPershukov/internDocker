
from django.core.serializers.json import Serializer
from django.core.serializers.python import Serializer as PSerializer
from vocabulary.models import *
import json

class ThemesSerialiser(Serializer):
    def __init__(self, showWords):
        self.showWords = showWords
    def end_object(self, obj):
        # self._current has the field data
        indent = self.options.get("indent")
        if not self.first:
            self.stream.write(",")
            if not indent:
                self.stream.write(" ")
        if indent:
            self.stream.write("\n")
        data = {}
        data['id'] = self._value_from_field(obj, obj._meta.pk)
        data.update(self._current)
        if (self.showWords ==True):
            wordSerializer = PythonWordSerializer()
            data['words']= wordSerializer.serialize(Theme.objects.get(pk=data['id']).word_set.all())

        json.dump(data, self.stream, **self.json_kwargs)
        self._current = None

class CategorySerialiser(Serializer):
    def end_object(self, obj):
        # self._current has the field data
        indent = self.options.get("indent")
        if not self.first:
            self.stream.write(",")
            if not indent:
                self.stream.write(" ")
        if indent:
            self.stream.write("\n")
        data = {}
        data['id'] = self._value_from_field(obj, obj._meta.pk)
        data.update(self._current)
        json.dump(data, self.stream, **self.json_kwargs)
        self._current = None

class LevelsSerialiser(Serializer):
    def end_object(self, obj):
        # self._current has the field data
        indent = self.options.get("indent")
        if not self.first:
            self.stream.write(",")
            if not indent:
                self.stream.write(" ")
        if indent:
            self.stream.write("\n")
        data = {}
        data['id'] = self._value_from_field(obj, obj._meta.pk)
        data.update(self._current)
        json.dump(data, self.stream, **self.json_kwargs)
        self._current = None
class WordSerialiser(Serializer):
    def end_object(self, obj):
        indent = self.options.get("indent")
        if not self.first:
            self.stream.write(",")
            if not indent:
                self.stream.write(" ")
        if indent:
            self.stream.write("\n")
        data = {}
        data['id'] = self._value_from_field(obj, obj._meta.pk)
        data.update(self._current)
        json.dump(data, self.stream, **self.json_kwargs)
        self._current = None

class PythonWordSerializer(PSerializer):
    def get_dump_object(self, obj):
        data = {'id': self._value_from_field(obj, obj._meta.pk)}
        data['name'] = self._current['name']
        return data