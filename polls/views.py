from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from tablib import Dataset
from .resources import PersonResource

from polls.models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name =  'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.filter(
                pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5] #Return the last 5 published Questions

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self): # Excludes any questions that aren't published yet.
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': p, 
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results',  args=(p.id,)))

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    ##response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    ##response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response