from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('src.web_app.urls', namespace='web_app')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('src.api.urls', namespace='api')),
]
