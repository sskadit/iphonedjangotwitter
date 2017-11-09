from django.shortcuts import render

# Create your views here.
from .models import AppleTrendingHastags,IphoneX
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import StreamingHttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import Context


def landing(request):
	
	queryset_list = AppleTrendingHastags.objects.all().order_by("created").distinct()

	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {

		"object_list": queryset,
	}
	return render(request, "landing.html",context)



def iphone(request):
	
	queryset_list = IphoneX.objects.all().order_by("created").distinct()

	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {

		"object_list": queryset,
	}
	return render(request, "iphone.html",context)