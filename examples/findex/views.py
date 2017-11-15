from django.shortcuts import render
import mongoengine

# Create your views here.
from django.http import HttpResponse


def index(request):

	mydb = mongoengine.connect(db='examples')
	#examples = mydb.objects()
	#print(examples)
	#count = examples.count()

	#print("There are %d examples in the database." % count)
	#qry = mongoengine.queryset.QuerySet()
	return HttpResponse("Hello, world. You're at the find example index.")