from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/', include('contact.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^blog/', include('blog.urls'))
]

urlpatterns += staticfiles_urlpatterns()
