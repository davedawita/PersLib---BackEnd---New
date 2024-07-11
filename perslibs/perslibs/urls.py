"""
URL configuration for perslibs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from perslib.views import YearViewSet, TitleViewSet, PerslibViewSet
# from perslib import views
from django.conf import settings   #Added for the purpose of profile picture or /static in seetings.py
# from django.conf.urls.static import static    #ditto

#Notes:
#ViewSets allow the developer to concentrate on modeling the state and interactions of the API, and leave the URL construction to be handled automatically. ViewSet classes are almost the same thing as View classes, except that they provide operations such as retrieve, or update, and not method handlers such as get or put.

# Because we're using ViewSet classes rather than View classes, we actually don't need to design the URL conf ourselves. The conventions for wiring up resources into views and urls can be handled automatically, using a Router class. All we need to do is register the appropriate view sets with a router, and let it do the rest.https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers

#Now, we need to register the view set we created in views.py to the urls:
router = routers.DefaultRouter()

router.register(r'year',YearViewSet)     
router.register(r'title',TitleViewSet)   
router.register(r'perslib',PerslibViewSet) 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)), #Here, we include all the urls which are in the router above
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    #This is added for adding pictures
