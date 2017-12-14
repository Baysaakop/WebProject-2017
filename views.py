
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Student
from .forms import NewStudentForm

def home(request):
	return render(request, 'home.html')

def list(request):
	student = Student.objects.all()
	return render(request, 'list.html', {'student': student})

def register(request):
	if request.method == 'POST':
		form = NewStudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list')
	else:
		form = NewStudentForm()
		return render(request, 'register.html', {'form': form})

def student_info(request, pk):
	student = get_object_or_404(Student, pk = pk)
	return render(request, 'student_info.html', {'student': student})
