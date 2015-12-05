from django.conf.urls import patterns, include, url

urlpatterns = patterns('beers_alt.views',
    url(r'^$', 'all_drinkers'),
    url(r'^all-drinkers$', 'all_drinkers'),
    url(r'^ingredient$', 'ingredient'),
    url(r'^home_page/(?P<current_user>[^/]+)$', 'home_page'), #grant = current
    url(r'^drinker/(?P<drinker_name>[^/]+)$', 'drinker'),
    url(r'^edit-drinker/(?P<drinker_name>[^/]+)$', 'edit_drinker'),
    url(r'^edit-drinker-submit/(?P<drinker_name>[^/]+)$', 'edit_drinker_submit'),
)
