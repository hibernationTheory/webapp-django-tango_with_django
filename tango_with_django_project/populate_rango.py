import os

CATEGORIES = {
'Python':
	[
	("Official Python Tutorial", "http://docs.python.org/2/tutorial/"),
	("How to Think like a Computer Scientist", "http://www.greenteapress.com/thinkpython/"),
	("Learn Python in 10 Minutes", "http://www.korokithakis.net/tutorials/python/")
	], {"views":128, "likes":15}
'Django':
	[
	("Official Django Tutorial", "https://docs.djangoproject.com/en/1.5/intro/tutorial01/"),
	("Django Rocks", "http://www.djangorocks.com/"),
	("How to Tango with Django", "http://www.tangowithdjango.com/")
	], {"views":1267, "likes":911}
'Other Frameworks':
	[
	("Bottle", "http://bottlepy.org/docs/dev/"),
	("Flask", "http://flask.pocoo.org")
	], {"views":25, "likes":2}
}

def populate():

	for i in CATEGORIES.iteritems():
		python_cat = add_cat(i[0])
		for j in i[1]:
			add_page(cat=python_cat, title=j[0], url=j[1])

	# Print out what we have added to the user.
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
	return p

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c

# Start execution here!
if __name__ == '__main__':
	print "Starting Rango population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
	from rango.models import Category, Page
	populate()