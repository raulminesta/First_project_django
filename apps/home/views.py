from django.shortcuts import render
from django.shortcuts import render
def index(request):
	context = {
		'users': [
			{ 'content': 'My name is Michael Choi'},
			{ 'content': 'I like to play Basketball'},
			{ 'content': 'My favorite programming langauge is Python'},
		]
	}
	return render(request, 'home/index.html', context)
