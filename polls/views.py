from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	#return HttpResponse(template.render(context,request))
	return render(request,'polls/index.html',context)


def detail(request,question_id):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")

	#return render(request,'polls/details.html',{'question': question})

	#return HttpResponse("You are looking at question %s" %question_id)
	question= get_object_or_404(Question,pk = question_id)
	return render(request,'polls/details.html',{'question': question})





def results(request,question_id):
	#r = "You are looking at the results of question %s"
	#return HttpResponse(r % question_id)
	question = get_object_or_404(Question,pk = question_id)
	return render(request, "polls/results.html", {'question': question})



def vote(request,question_id):
	#return HttpResponse("THe number of votes  for %s are  x"%question_id)
	p = get_object_or_404(Question, pk= question_id)
	try:
		selected_choice = p.choice_set.get(pk= request.POST['choice'])
	except (Keyerror, Choice.DoesNotExist):
		return render(request, polls/details.html,{
			'question': p,
			'error_message': "You didn't select a choice",
			})	
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse("polls:results", args=(p.id,)))