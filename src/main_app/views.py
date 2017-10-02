from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
#Class-based view
class TemplateView(TemplateView):
    """The default template name will be index and loaded on root"""
    template_name = "index.html"
    def get_context_data(self, *args, **kwargs): #request
        """context reffers to this view"""
        context = super(TemplateView, self).get_context_data(*args, **kwargs)
        context = self.get_context_by_template_name(self.template_name)
        return context
    
    def get_context_by_template_name(self, template_name):
        if(template_name == 'index.html'):
            context = {
                'page_title' : "Login"
            }
        else:
            context = {
                "page_title" : "Dashboard",
                "variable" : "Items"
            }
        return context

        