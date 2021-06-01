from django.shortcuts import render
from .models import Member

# Create your views here.
def Members(request):
    Members = Member.objects.all()
    return render(request, 'Members.html', {'Member': Members})