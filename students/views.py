from django.shortcuts import render_to_response
from django.shortcuts import render


# Create your views here.
def student_index(request):
    return render_to_response('index.html')