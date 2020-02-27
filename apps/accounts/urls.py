from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

import apps.accounts.views

app_name='accounts'

urlpatterns = [
  url(_(r'^signup/$'),
    apps.accounts.views.UserRegisterView.as_view(),
    name='user_signup'),

]
