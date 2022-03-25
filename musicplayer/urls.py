
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from loginform.views import login_users
from signupforms.views import user_register
from homepage.views import home_view,addfavs_view,getsong_lyrics,logout_view
from favourites.views import favourite_view
from uploadsongs.views import uploads_view
from profiles.views import profiles_view,update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_users,name= "userlogin"),
    path('user_register/', user_register, name = "userregister"),
    path('home/',home_view, name="home"),
    path('favourites/',favourite_view, name= "favourites"),
    path('uploadsongs/',uploads_view, name= "uploads"),
    path('profiles/',profiles_view, name="profiles"),
    path('updateprofile/',update_view,name="updateprofile"),
    path('savefavourites/<int:id>',addfavs_view,name = "savefavourites"),
    path('searchlyrics/<int:id>',getsong_lyrics, name="getlyrics"),
    path('logout',logout_view,name="logout")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

