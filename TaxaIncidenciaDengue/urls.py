from django.conf.urls import patterns, url

urlpatterns = patterns(
    'TaxaIncidenciaDengue.views',
        url(r'^getTaxaIncidenciaDengue/$', 'getTaxaIncidenciaDengue', name='getTaxaIncidenciaDengue'),
)