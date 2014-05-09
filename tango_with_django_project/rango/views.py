# Create your views here.
from django.http import HttpResponse

def index(request):
	response = '''Rango says: Hello World!, 
		here is a page to visit for you: <a href="about/">About</a>'''
	return HttpResponse("%s" %response)

def about(request):
	return HttpResponse("Rango Says: Here is the 'about' page")