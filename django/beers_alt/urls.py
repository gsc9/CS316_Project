from django.conf.urls import patterns, include, url

urlpatterns = patterns('beers_alt.views',
    url(r'^$', 'welcome'),
    url(r'^home_page/(?P<current_user>[^/]+)$', 'home_page'), #grant = current
 #   url(r'^home_page/user$', 'home_page'), #grant = current
    url(r'^all-drinkers$', 'all_drinkers'),
    url(r'^create-event$', 'create_event'),
    #url(r'^invite-form/(?P<eid>[^/]+)$', 'invite_form'),
    url(r'^invite-form$', 'invite_form'),
    url(r'^login$', 'login'),
    url(r'^register$', 'register'),
    url(r'^logout$', 'logout'),
    url(r'^event/(?P<eid>[^/]+)$', 'event'),
    url(r'^bring-ingredient$', 'bring_form'),
    url(r'^add-ingredient$', 'add_form'),
    url(r'^drinker/(?P<drinker_name>[^/]+)$', 'drinker'),
    url(r'^edit-drinker/(?P<drinker_name>[^/]+)$', 'edit_drinker'),
    url(r'^edit-drinker-submit/(?P<drinker_name>[^/]+)$', 'edit_drinker_submit'),
)
