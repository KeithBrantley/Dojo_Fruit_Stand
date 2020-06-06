from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout_page),
    # path('checkout', views.checkout),
    path('checkout/<int:check_out_total>', views.check_total),
    path('go_home', views.direct_to_index),
]