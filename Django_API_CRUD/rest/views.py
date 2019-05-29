import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.core.serializers import serialize

from .models import Update
from .mixins import JsonResponseMixin


def list_view(request):
    obj = Update.objects.all()
    data = {
        'obj':obj,
    }
    return render(request, 'list.html', context=data)

def detail_view(request, id):
    obj = Update.objects.get(pk=id)
    data = {
        'obj':obj,
    }
    return render(request, 'detail.html', context=data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            'user':'sagar',
            'content':'posts',
        }
        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            'user': 'sagar',
            'content': 'posts',
        }
        return self.render_to_json_response(data)


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        #data = serialize('json', qs, fields=('user', 'content'))
        # print(data)
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(pk=1)
        # data = {
        #     'user':obj.user.username,
        #     'content':obj.content,
        # }
        # json_data = json.dumps(data)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')
