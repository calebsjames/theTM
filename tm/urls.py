from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from tmapi.views.auth import register_user, login_user
from tmapi.views import ContactNoteView, HotelView, PromoterView, ScheduleView, ShowView, VenueView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'contactnotes', ContactNoteView, 'contactnote')
router.register(r'hotels', HotelView, 'hotel')
router.register(r'promoters', PromoterView, 'promoter')
router.register(r'schedules', ScheduleView, 'schedule')
router.register(r'shows', ShowView, 'show')
router.register(r'venues', VenueView, 'venue')
# router.register(r'users', VenueView, 'venue')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
