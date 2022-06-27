from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .forms import Mform
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from .models import InputModel
# Create your views here.
def create_view(request):
    context={}
    templ=loader.get_template('home.html')
    form=Mform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list'))
    context['form']=form
    return HttpResponse(templ.render(context,request))
def list_view(request):
    context={}
    templ=loader.get_template('list_view.html')
    context['dataset']=InputModel.objects.all()
    return HttpResponse(templ.render(context,request))
def detail_view(request,id):
    context={}
    templ=loader.get_template('detail_view.html')
    context['query']=InputModel.objects.get(id=id)
    return HttpResponse(templ.render(context,request))
def update_view(request,id):
    context={}
    templ=loader.get_template('update_view.html')
    obj=get_object_or_404(InputModel,id=id)
    form=Mform(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list'))
    context['form']=form
    return HttpResponse(templ.render(context,request))
def delete_view(request,id):
    context={}
    templ=loader.get_template('delete_view.html')
    obj=get_object_or_404(InputModel,id=id)

    if request.method=='POST':
        obj.delete()
        return HttpResponseRedirect(reverse('list'))
    return HttpResponse(templ.render(context,request))
