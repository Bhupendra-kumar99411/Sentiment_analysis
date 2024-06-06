from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import UploadJsonView, UploadTweet

urlpatterns = [
    path("", views.index, name="Index Page"),
    path("docs", views.docs, name="Docs"),
    path("orders", views.orders, name="Orders"),
    path("notifications", views.notifications, name="Notifications"),
    path("account", views.account, name="Account"),
    path("settings", views.settings, name="Settings"),
    path("login", views.login, name="Login"),
    path("signup", views.signup, name="Signup"),
    path("reset-password", views.reset_password, name="reset-password" ),
    path("404", views.error, name="Error 404"),
    path("charts", views.charts, name="Charts" ),
    path("help", views.help, name="help"),
    path('upload/', UploadJsonView.as_view(), name='upload_json'),
    path('uploadtweets/', UploadTweet.as_view(), name='upload tweet'),
    path('upload_data', views.main, name='upload'),
    path("sent", views.sentiment, name="sentiment"),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)