from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_AIPN/', views.about_aipn, name='about_aipn'),
    path('mission_and_vision/', views.mission, name='mission'),
]

'''
    path('Contact_Us/', views.contact_us, name='contact_us'),
    path('board_of_directors/', views.board, name='board'),
    path('committees/', views.committees, name='committees'),
    path('Why_CFA/', views.why_cfa, name='why_cfa'),
    path('about_CFA/', views.about_cfa, name='about_cfa'),
    path('about_CIPM/', views.about_cipm, name='about_cipm'),
    path('Investment_Foudnation/', views.invetment_foundation, name='invetment_foundation'),
    path('Exam_Fees/', views.exam_fees, name='exam_fees'),
    #path('about_us/', views.about_us, name='about_us'),
    #path('about_us/', views.about_us, name='about_us'),
    #path('about_us/', views.about_us, name='about_us'),
'''
