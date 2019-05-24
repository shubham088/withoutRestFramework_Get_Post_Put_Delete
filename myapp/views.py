# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from myapp.models import Employee
#from django.core.serializers import serialize
from .mixins import SerializerMixin
from .utils import is_json
from .forms import EmployeeForm
# Create your views here.

class EmployeeDetailCBV(SerializerMixin,View):

    #to get the records by id
    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        #json_data = serialize('json', [emp,])
        json_data = self.serialize([emp,])
        return HttpResponse(json_data, content_type='application/json')

    #for update record
    def put(self, request, id, *args, **kwargs):
        #check if emp exists or not
        emp = self.get_object_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'Employee Does Not Exist'})
            return HttpResponse(json_data, content_type='application/json')
        data = request.body
        valid = is_json(data)
        if not valid:
            json_data = json.dumps({'msg':'Data Provided is not valid'})
            return HttpResponse(json_data, content_type='application/json')
        provided_data = json.loads(data)
        original_data = {
            'eno' : emp.eno,
            'ename' : emp.ename,
            'esal' : emp.esal,
            'eaddr' : emp.eaddr
            }
        original_data.update(provided_data)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg':'Record Updated Successfully'})
            return HttpResponse(json_data, content_type='application/json')


    def delete(self, request, id, *args, **kwargs):
        #check if emp exists or not
        emp = self.get_object_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'Employee Does Not Exist'})
            return HttpResponse(json_data, content_type='application/json')
        status, deleted_obj = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg':'Employee Deleted Successfully'})
            return HttpResponse(json_data, content_type='application/json')
        json_data = json.dumps({'msg':'Employee Cant be Deleted. '})
        return HttpResponse(json_data, content_type='application/json')


    def get_object_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except DoesNotExist:
            emp = None
        return emp


class EmployeeListCBV(SerializerMixin,View):

    #to get all the records
    def get(self, request, *args, **kwargs):
        emp = Employee.objects.all()
        json_data = self.serialize(emp)
        return HttpResponse(json_data, content_type='application/json')

    #to update new record
    def post(self,request, *args, **kwargs):
        data = request.body
        valid = is_json(data)
        if not valid:
            json_data = json.dumps({'msg':'Please give data in correct format'})
            return HttpResponse(json_data, content_type='application/json')
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save()
            json_data = json.dumps({'msg':'Resource Created Successfully.'})
            return HttpResponse(json_data, content_type='application/json')
