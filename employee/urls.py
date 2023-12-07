from django.contrib import admin  
from django.urls import path  
from employee import views 
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('accept/<int:id>', views.accept),  
     path('signup2/<int:id>', views.signup2),
    path('delete/<int:id>', views.destroy), 
    path('signup', views.signup), 
    path('requests', views.requests),
    path('main', views.main),
    path('reset_password', views.reset_password),
    path('reset_password_admin', views.reset_password_admin),
    path('logout', views.logoutpage, name='logout'),
    path('showresult', views.showresult),
    path('showhistory', views.showhistory, name='showhistory'),
    path('showhistoryadmin', views.showhistoryadmin, name='showhistoryadmin'),
    path('showresultformainadmin', views.showresultformainadmin),
    path('showresultforsuperadmin', views.showresultforsuperadmin),
    path('preprocess', views.preprocess),
    path('deletephoto/<int:id>', views.destroy2),
    path('deleteall', views.deleteall),
    path('deletephoto1/<int:id>', views.destroy3),
    path('deleteall1', views.deleteall1),
    #path('entercode', views.entercode),
    
    
    
    
    
    
    

    
]  
#if settings.DEBUG:
 #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)