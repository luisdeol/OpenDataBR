from django.conf.urls import patterns, url

urlpatterns = patterns(
    'TaxaIncidenciaDengue.views',
    url(r'^getTaxaIncidenciaDengueUF/$', 'getTaxaIncidenciaDengueUF', name='getTaxaIncidenciaDengueUF'),
    url(r'^getTaxaIncidenciaDengueBrasil/$', 'getTaxaIncidenciaDengueBrasil', name='getTaxaIncidenciaDengueBrasil'),
    url(r'^getTaxaIncidenciaDengueCapitais/$', 'getTaxaIncidenciaDengueCapitais', name='getTaxaIncidenciaDengueCapitais')
)