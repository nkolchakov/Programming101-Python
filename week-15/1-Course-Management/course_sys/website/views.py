from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
def show_course(request, course_name):
    wanted_course = Course.objects.filter(name = course_name)
    if not len(wanted_course) > 0:
    	return HttpResponse('No such course in database, please create it')
    
    name = wanted_course[0].name
    desct = wanted_course[0].description
    st_date = wanted_course[0].start_date
    end_date = wanted_course[0].end_date

    course_field = wanted_course[0]
    json = course_field.__dict__

    return render(request, 'show_course_table.html', locals())


def edit_course(request, course_name):
	return HttpResponse('here we will edit {}'.format(course_name))

def create_course(request):
	if request.method == 'POST':
		name = request.POST['name']
		descr = request.POST['descr']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		if Course.exists(name):
			return HttpResponse('course already exists')
		else:
			c = Course(name, descr, start_date, end_date)
			c.save()

	return render(request, 'create_new.html')

def home(request):
    return HttpResponse('Welcome to home page')