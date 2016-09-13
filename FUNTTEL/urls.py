from django.conf.urls import patterns, url

urlpatterns = patterns(
    'FUNTTEL.views',
        url(r'^getTaxaRetorno/$', 'getTaxaRetorno', name='getTaxaRetorno'),
        url(r'^getGeracaoEmprego/$', 'getGeracaoEmprego', name='getGeracaoEmprego'),
)