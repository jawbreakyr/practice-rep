from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question


# def index(request):
# 	latest_question_list = Question.objects.order_by("-pub_date")[:5]
# 	# output = ", ".join([q.question_text for q in latest_question_list])
# 	# parse each object with comma
# 	template = loader.get_template("polls/index.html")
# 	context = {
# 		"latest_question_list": latest_question_list,
# 	}
# 	return HttpResponse(template.render(context, request))

# shortcut render
def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	context = {
		"latest_question_list": latest_question_list,
	}
	return render(request, "polls/index.html", context)

# def detail(request,question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question Does Not Exist Mother Fucker!!")
	
# 	return render(request, "polls/detail.html", {"question": question})

# shortcut render && get_object_or_404
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	# for i in dir(question):
	# 	print(i)
	return render(request, "polls/detail.html", {"question":question})

def results(request, question_id):
	response = "You're looking at results of question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % question_id)