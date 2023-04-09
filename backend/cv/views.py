from django.views.generic.base import TemplateView


class MaxxtorCvView(TemplateView):
    template_name = 'maxxtor.html'


class AlexshowCvView(TemplateView):
    template_name = 'alexshow.html'
