from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from encuestas.models import Poll, Choice

# Create your views here.
def index(request):
	latest_poll_list = Poll.objects.order_by("-pub_date")[:5]
	#template = loader.get_template("encuestas/index.html")
	#output = ', '.join([p.question for p in latest_poll_list])
	context = {'latest_poll_list': latest_poll_list,}
	return render(request,'encuestas/index.html',context)

def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'encuestas/detalles.html', {'poll': poll})

def resultados(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'encuestas/resultados.html', {'poll': poll})

def votos(request, poll_id):
	p=get_object_or_404(Poll,pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'encuestas/detalles.html',{
			'poll':p,
			'error_message': "No has seleccionado ninguna alternativa.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('encuestas:resultados',args=(p.id,)))


