from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
router = routers.DefaultRouter()
#router.register('userblog', views.UserViewSet)
router.register('resume', views.Resumeblog)


urlpatterns = [
    #path('loginapiblogdata/', views.UserViewSet.as_view()),
    #path('resume', views.Resumeblog.as_view() ),
    path('blogapi', include(router.urls)),  
    path('checkpermission/', views.checkpermission),
    

    
    
    #path('city', views.Genericcity.as_view(), name ='city'),
    #path('datalogin', views.UserViewSet.as_view({'get': 'list'})),
    path('blogapilogin/', views.CustomAuthTokenLogin.as_view()),
    path('', views.homepage, name ='homepage'),
    path('register', views.register, name ='hello'),
    path('api/', views.Blogapi.as_view(), name ='hello'),
    path('Relationship/', views.Relationship.as_view(), name ='rel'),
     path('login', views.login, name ='hello'),
    path('add', views.addblog, name ='addblog'),

    path('insertblog',views.insertblog,name='insertblog'), 
    path('editblogform', views.updateblog, name ='addblog'),
    
    path('readblogdata/<int:id>', views.readblogdata, name ='readblogdata'),

    path('editBlog/<int:id>', views.editBlog,name='editBlog'), 
    path('deleteblog',views.deleteblog,name='deleteblog'), 

    path('dashboard', views.dashboard, name ='hello'),
   
    path('adduser', views.adduser, name ='adduser'),

    path('logout',views.logout,name='logout'),


	#path('hello/', views.HelloView.as_view(), name ='hello'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
