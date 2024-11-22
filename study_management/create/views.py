# views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView , ListView , UpdateView , DetailView , DeleteView
from .models import createstudy
from .forms import createstudyform
from django.shortcuts import get_object_or_404 ,redirect 
from django.http import HttpResponseForbidden ,JsonResponse

class CreateStudyFormView(CreateView):
    model = createstudy
    form_class = createstudyform
    template_name = 'createstudy.html'
    success_url = reverse_lazy('createstudyformview')


class ShowStudyFormView(ListView):
    model = createstudy
    template_name = 'show_study.html' 
    context_object_name = 'users'
    
class UpdateStudyFormView(UpdateView):
    model = createstudy
    form_class = createstudyform
    template_name = 'edit_study.html'
    context_object_name = 'study_form'    
    success_url = reverse_lazy('showstudyformview') 
    
   
class Detailstudy(DetailView):
    model = createstudy
    template_name = 'detail_study.html'
    context_object_name = 'studydata'
    pk_url_kwarg = 'pk'

def DeleteNote(request,pk):
      
        if request.method == "POST":
          choosed_id = get_object_or_404(createstudy,pk=pk)
          choosed_id.delete()
          return redirect('showstudyformview') 
        else:
          return HttpResponseForbidden("Invalid request method.")

def DeleteAll(request):
        
        if request.method == "POST":
            all_data = createstudy.objects.all()
            all_data.delete()
            return redirect('showstudyformview')
        else:
          return HttpResponseForbidden("Invalid request method.") 