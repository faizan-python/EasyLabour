from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from user_auth import views

urlpatterns = [
    url(r'^user/register/$', views.CreateUserView.as_view(),
        name='create_user'),
    # url(r'^user/social/register/$', views.CreateSocialUserView.as_view(),
    #     name='create_social_user_register_login'),
    url(r'^user/login/$', views.LoginView.as_view(),
        name='login'),
    # ## this we have kept so that name of url
    # ## doesnt show functionality of same
    # ## preventing unauthorized access of same
    # url(r'^user/clean-data/$', views.RefreshOauthToken.as_view(),
    #     name='get_new_token'),
    # url(r'^user/update-pwd/$', views.UserUpdatePassword.as_view(),
    #     name='update_pwd'),
    # url(r'^forgot/password/$', views.ForgotPasswordView.as_view(),
    #     name='forgot_password'),
    # url(r'^forgot/change-password/$',
    #     views.UserForgotPasswordChangeView.as_view(),
    #     name='forgot_change_password'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
