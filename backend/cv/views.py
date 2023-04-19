from django.views.generic.base import TemplateView


class MaxxtorCvView(TemplateView):
    template_name = 'cv/maxxtor.html'


class AlexshowCvView(TemplateView):
    template_name = 'cv/alexshow.html'
