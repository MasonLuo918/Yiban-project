from django.conf.urls import url
from . import views as account_views
from django.contrib.auth import views as auth_views
app_name = "account"

urlpatterns = [
    url(r'^register/$',account_views.register,name="register"),
   # url(r'^login/$',account_views.user_login,name="login"),
    url(r'^login/$',auth_views.login,{"template_name":"account/login.html"},name="login"),
    url(r'^logout/$',auth_views.logout,{"template_name":"account/logout.html"},name="logout"),
    url(r'^password-change/$',auth_views.password_change,{"template_name":"account/password-change.html","post_change_redirect":"account:password-change-done"},name="password-change"),
    url(r'^password-change-done/$',auth_views.password_change_done,{"template_name":"account/password-change-done.html"},name="password-change-done"),
    url(r'^success/$',account_views.success,name="RegisterSuccess"),
    url(r'^failure/$',account_views.failure,name="RegisterFailure"),
    url(r'^password-reset/$',auth_views.password_reset,
        {"template_name":"account/password_reset_form.html",
          "email_template_name":"account/password_reset_email.html",
          "subject_template_name":"account/subject_template_name.txt",
         "post_reset_redirect":"/account/password-reset-done"
         },
        name="password_reset",
        ),
    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,
        {"template_name":"account/password_reset_confirm.html","post_reset_redirect":"/account/password-reset-complete"},
        name="password_reset_confirm"
        ),

    url(r'^password-reset-done/$',auth_views.password_reset_done,{"template_name":"account/password_reset_done.html"},name="password_reset_done"),
    url(r'^password-reset-complete/$',auth_views.password_reset_complete,{"template_name":"account/password_reset_complete.html"},name="password_reset_complete"),
    url(r'^myself/$',account_views.myself,name="myself"),
    url(r'^edit-myself/$',account_views.editmyself,name="editmyself"),
    url(r'my-image/$',account_views.my_image,name="my_image"),
]