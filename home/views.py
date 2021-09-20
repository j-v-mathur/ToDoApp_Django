from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import todo


def index(request):
	if request.method=="POST":
		title = request.POST.get("title")
		desc = request.POST.get("desc")
		data = todo(title=title,desc=desc)
		data.save()

	td = todo.objects.all()
	params = {'td':td}
	return render(request,"index.html",params)

def detail(request):
	if request.method=="GET":
		global val
		val = request.GET.get("id")
		q = todo.objects.filter(id=val)
		params = {'q':q}
	
	if request.method=="POST" and "update" in request.POST:
		title = request.POST.get("title")
		desc = request.POST.get("desc")
		obj = todo.objects.get(id=val)
		obj.title = title
		obj.desc = desc
		obj.save()
		q = todo.objects.filter(id=val)
		params = {'q':q}
		
	if request.method=='POST' and 'delete' in request.POST:
		todo.objects.filter(id=val).delete()
		return redirect("/")
	
	return render(request,"detail.html",params)