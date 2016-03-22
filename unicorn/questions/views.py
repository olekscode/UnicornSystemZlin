from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question, Answer


class IndexView(generic.ListView):
	template_name = 'questions/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'questions/detail.html'


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'questions/results.html'


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_answer = question.answer_set.get(pk=request.POST['answer'])
	except (KeyError, Answer.DoesNotExist):
		# Redisplay the question voting form
		return render(request, 'questions/detail.html', {
			'question': question,
			'error_message': "You didn't select an answer",
		})
	else:
		selected_answer.votes += 1
		selected_answer.save()
		return HttpResponseRedirect(reverse('questions:results',
			args=(question.id,)))

# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	context = {
# 		'latest_question_list': latest_question_list,
# 	}
# 	return render(request, 'questions/index.html', context)

# def detail(request, question_id):
# 	try:
# 		question = Question.objects.get(pk=question_id)
# 	except Question.DoesNotExist:
# 		raise Http404("Question does not exist")

# 	context = {
# 		'question': question,
# 		'answers': Answer.objects.filter(question=question),
# 	}
# 	return render(request, 'questions/detail.html', context)

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'questions/results.html', {'question': question})