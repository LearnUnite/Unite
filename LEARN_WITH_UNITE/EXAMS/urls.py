from django.urls import path
from . import views

app_name = 'EXAMS'

urlpatterns =[
    path('biology/form5', views.biology_form5.as_view() , name='bio_form5'),
    path ('create_exams_biology-F5/',views.CreateBiology_Form5Exams.as_view(), name='create_bio5'),
    path('delete_exams_biology-F5/(?P<pk>\d+)/$', views.DeleteBiology_Form5Exams , name='delete_bio5'),
    
    path('chemistry/form5', views.chemistry_form5.as_view() , name='chem_form5'),
    path ('create_exams_chemistry-F5/',views.CreateChemistry_Form5Exams.as_view(), name='create_chem5'),
    path('delete_exams_chemistry-F5/(?P<pk>\d+)/$', views.DeleteChemistry_Form5Exams , name='delete_chem5'),

    path('economics/form5', views.economics_form5.as_view() , name='eco_form5'),
    path ('create_exams_economics-F5/',views.CreateEconomics_Form5Exams.as_view(), name='create_eco5'),
    path('delete_exams_economics-F5/(?P<pk>\d+)/$', views.DeleteEconomics_Form5Exams , name='delete_eco5'),

    path('general_studies/form5', views.general_studies_form5.as_view() , name='gs_form5'),
    path ('create_exams_general_studies-F5/',views.CreateGeneral_Studies_Form5Exams.as_view(), name='create_gs5'),
    path('delete_exams_general_studies-F5/(?P<pk>\d+)/$', views.DeleteGeneral_Studies_Form5Exams , name='delete_gs5'),

    path('geography/form5', views.geography_form5.as_view() , name='geo_form5'),
    path ('create_exams_geography-F5/',views.CreateGeography_Form5Exams.as_view(), name='create_geo5'),
    path('delete_exams_geography-F5/(?P<pk>\d+)/$', views.DeleteGeography_Form5Exams , name='delete_geo5'),

    path('history/form5', views.history_form5.as_view() , name='his_form5'),
    path ('create_exams_history-F5/',views.CreateHistory_Form5Exams.as_view(), name='create_his5'),
    path('delete_exams_history-F5/(?P<pk>\d+)/$', views.DeleteHistory_Form5Exams , name='delete_his5'),

    path('kiswahili/form5', views.kiswahili_form5.as_view() , name='kis_form5'),
    path ('create_exams_kiswahili-F5/',views.CreateKiswahili_Form5Exams.as_view(), name='create_kis5'),
    path('delete_exams_kiswahili-F5/(?P<pk>\d+)/$', views.DeleteKiswahili_Form5Exams , name='delete_kis5'),

    path('language/form5', views.language_form5.as_view() , name='lang_form5'), 
    path ('create_exams_language-F5/',views.CreateLanguage_Form5Exams.as_view(), name='create_lang5'),
    path('delete_exams_language-F5/(?P<pk>\d+)/$', views.DeleteLanguage_Form5Exams , name='delete_lang5'),

    path('mathematics/form5', views.mathematics_form5.as_view() , name='math_form5'), 
    path ('create_exams_mathematics-F5/',views.CreateMathematics_Form5Exams.as_view(), name='create_math5'),
    path('delete_exams_mathematics-F5/(?P<pk>\d+)/$', views.DeleteMathematics_Form5Exams , name='delete_math5'),

    path('physics/form5', views.physics_form5.as_view() , name='phy_form5'),
    path ('create_exams_physics-F5/',views.CreatePhysics_Form5Exams.as_view(), name='create_phy5'),
    path('delete_exams_physics-F5/(?P<pk>\d+)/$', views.DeletePhysics_Form5Exams , name='delete_phy5'),
   
]