from django.views.generic import TemplateView


class CreateCardView(TemplateView):
    template_name = 'create_card.html'


class LandingView(TemplateView):
    template_name = 'landing.html'
