from django.conf.urls import url
from routing.views import (
    simple_route, slug_route, sum_route,
    sum_get_method, sum_post_method,
)

urlpatterns = [
    url('^simple_route/$', simple_route),
    url(r'^slug_route/([0-9a-z_-]{,16})/$', slug_route),
    url(r'^sum_route/(-?\d+)/(-?\d+)/$', sum_route),
    url(r'^sum_get_method/$', sum_get_method),
    url(r'^sum_post_method/$', sum_post_method)
]
