from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request, 'Input.html')

def output(request):
    team = request.GET['teamName']
    teamName = team.split(", ")
    count = len(teamName)
    index = 0
    return render(request, 'Output.html', { 'teamName' : teamName, 'count' : count })