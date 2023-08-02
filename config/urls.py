from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
        path('', TemplateView.as_view(template_name='index.html'), name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #追加 nomura
