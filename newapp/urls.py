from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter



router=DefaultRouter()


router.register("viewseturl",todoviewsets,basename='todoviewsets'),
router.register("newyseturl",newyviewsets,basename='newyviewsets'),
router.register("personseturl",personview,basename='personview')



urlpatterns=[
    path('new/',new.as_view()),
    path('detail/<pk>',newdetail.as_view()),
    path('hotel/',hotelview.as_view()),
    path('hotdetail/<pk>',hotdetail.as_view()),
    path('pro/',productview.as_view()),
    path('pro2/<id>',prody.as_view()),
    path('employee/',empview),
    path('employ/<id>',emplodet)




]+(router.urls)
