import json
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from rest.models import Update

from rest.forms import UpdateModelForm
from rest.mixins import HttpResponseMixin
from .mixins import CSRFExemptMixin
from .utils import is_json

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):

    is_json = True

    def get_object(self, pk=None):
        # try:
        #     obj = Update.objects.get(pk=pk)
        # except Update.DoesNotExist:
        #     obj = None
        qs = Update.objects.filter(pk=pk)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(pk=id)
        if obj is None:
            error_data = json.dumps({'message':"Update not found"})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def put(self, request, id, *args, **kwargs):
        # print(request.body)
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message': "Invalid data sent, please use JSON format"})
            return self.render_to_response(error_data, status=400)

        obj = self.get_object(pk=id)
        if obj is None:
            error_data = json.dumps({'message': "Update not found"})
            return self.render_to_response(error_data, status=404)
        # print(dir(request))

        # new_data = {}
        data = json.loads(obj.serialize())
        # saved_data = {
        #     'user':obj.user,
        #     'content':obj.content,
        # }
        passed_data = json.loads(request.body)
        for key, value in passed_data.items():
            data[key] = value
        print(passed_data)

        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        json_data = json.dumps({'message':"something put"})
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):

        json_data = json.dumps({'message':"not allowed, you can use /rest/api endpoint"})
        return self.render_to_response(json_data, status=403)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(pk=id)
        if obj is None:
            error_data = json.dumps({'message': "Data not found"})
            return self.render_to_response(error_data, status=404)

        deleted, item_deleted = obj.delete()
        print(deleted)
        if deleted == 1:
            json_data = json.dumps({'message':"successfully deleted"})
            return self.render_to_response(json_data, status=200)
        error_data = json.dumps({'message': "some error, please try again later."})
        return self.render_to_response(error_data, status=403)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):

    is_json = True
    queryset = None

    def get_queryset(self):
        qs = Update.objects.all()
        self.queryset = qs
        return qs

    def get_object(self, pk=None):
        # try:
        #     obj = Update.objects.get(pk=pk)
        # except Update.DoesNotExist:
        #     obj = None
        if id is None:
            return None
        qs = self.get_queryset().filter(pk=pk)
        if qs.count() == 1:
            return qs.first()
        return None


    def get(self, request, *args, **kwargs):
        data = json.loads(request.body)
        passed_id = data.get('pk', None)
        if passed_id is not None:
            obj = self.get_object(pk=passed_id)
            if obj is None:
                error_data = json.dumps({'message': "Object not found"})
                return self.render_to_response(error_data, status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        else:
            qs = self.get_queryset()
            # qs2 = Update.objects.filter(id__gte=2)
            json_data = qs.serialize()
            return self.render_to_response(json_data, status=200)

    def post(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message': "Invalid data sent, please use JSON format"})
            return self.render_to_response(error_data, status=400)

        data = json.loads(request.body)

        form = UpdateModelForm(data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        data = {"message":"is that possible tht form have no error and not valid?"}
        return self.render_to_response(data, status=400)

    def put(self, request, *args, **kwargs):

        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message': "Invalid data sent, please use JSON format"})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('pk', None)

        if not passed_id:
            error_data = json.dumps({'id': "this is required field to update item"})
            return self.render_to_response(error_data, status=400)

        obj = self.get_object(pk=passed_id)
        if obj is None:
            error_data = json.dumps({'message': "Object not found"})
            return self.render_to_response(error_data, status=404)
        # print(dir(request))

        # new_data = {}
        data = json.loads(obj.serialize())
        # saved_data = {
        #     'user':obj.user,
        #     'content':obj.content,
        # }
        for key, value in passed_data.items():
            data[key] = value
        print(passed_data)

        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        json_data = json.dumps({'message':"something put"})
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):

        valid_json = is_json(request.body)
        if not valid_json:
            error_data = json.dumps({'message': "Invalid data sent, please use JSON format"})
            return self.render_to_response(error_data, status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('pk', None)

        if not passed_id:
            error_data = json.dumps({'id': "this is required field to update item"})
            return self.render_to_response(error_data, status=400)

        obj = self.get_object(pk=passed_id)
        if obj is None:
            error_data = json.dumps({'message': "Object not found"})
            return self.render_to_response(error_data, status=404)

        deleted, item_deleted = obj.delete()
        print(deleted)
        if deleted == 1:
            json_data = json.dumps({'message': "successfully deleted"})
            return self.render_to_response(json_data, status=200)
        error_data = json.dumps({'message': "some error, please try again later."})
        return self.render_to_response(error_data, status=403)
