from django.shortcuts import render
from django.views import generic
from .models import Teacher, Course, Category, Location, Age_recommend
# Create your views here.
def home_page(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    # The 'all()' is implied by default.
    num_course= Course.objects.all().count()
    num_teacher = Teacher.objects.all().count()

    context = {
        'num_course': num_course,
        'num_teacher': num_teacher,
    }

    # Render the HTML template home_page.html with the data in the context variable
    return render(request, 'home_page.html', context=context)

#######################################

def location_list(request):
    location = Location.objects.all()
    context = {
        'locations': location,
    }

    return render(request,'location_list.html',  context=context)


#######################################    
# class CourseListView(generic.ListView):
#     model = Course
    
class CourseDetailView(generic.DetailView):
    model = Course

from django.shortcuts import get_object_or_404

def courseDetailView(request, primary_key):
    course = get_object_or_404(Course, pk=primary_key)
    return render(request, 'catalog/course_detail.html', context={'course': course})

#######################################
def about(request):
    History = "Kiddee Lab was founded in _____ "
    Vision = "Our vision is _____"
    Mission = "Our mission is ______"
    context = {
        'history': History,
        'vision': Vision,
        'mission': Mission
    }

    return render(request,'about.html',  context=context)
############################################################

def CourseListView(request):
    course = Course.objects.all()
    category = Category.objects.all()
    age = Age_recommend.objects.all()

    category_id = request.GET.get('category_list')
    age_id = request.GET.get('age_list')

    if category_id:
        course = Course.objects.filter(category=category_id)
    elif age_id:
        course = Course.objects.filter(age_recommend=age_id)
    else:
        course = Course.objects.all()


    context = {
        'course_list': course,
        'category_list': category,
        'age_list': age
    }
    return render(request, 'catalog/course_list.html',context=context)

#######################################

class TeacherDetailView(generic.DetailView):
    model = Teacher


def CourseListView(request):
    course = Course.objects.all()
    category = Category.objects.all()
    age = Age_recommend.objects.all()

    category_id = request.GET.get('category_list')
    age_id = request.GET.get('age_list')

    if category_id:
        course = Course.objects.filter(category=category_id)
    elif age_id:
        course = Course.objects.filter(age_recommend=age_id)
    else:
        course = Course.objects.all()


    context = {
        'course_list': course,
        'category_list': category,
        'age_list': age
    }
    return render(request, 'catalog/course_list.html',context=context)