from django.urls import path
from . import views

app_name = 'NOTES'

urlpatterns =[
    path('biology/form5', views.biology_form5.as_view() , name='bio_form5'),
    path ('create_notes_biology-F5/',views.CreateBiology_Form5Notes.as_view(), name='create_bio5'),   
    path('delete_notes_biology-F5/(?P<pk>\d+)/$', views.DeleteBiology_Form5Notes , name='delete_bio5'),
    
    path('chemistry/form5', views.chemistry_form5.as_view() , name='chem_form5'),
    path ('create_notes_chemistry-F5/',views.CreateChemistry_Form5Notes.as_view(), name='create_chem5'),
    path('delete_notes_chemistry-F5/(?P<pk>\d+)/$', views.DeleteChemistry_Form5Notes , name='delete_chem5'),

    path('economics/form5', views.economics_form5.as_view() , name='eco_form5'),
    path ('create_notes_economics-F5/',views.CreateEconomics_Form5Notes.as_view(), name='create_eco5'),
    path('delete_notes_economics-F5/(?P<pk>\d+)/$', views.DeleteEconomics_Form5Notes , name='delete_eco5'),

    path('general_studies/form5', views.general_studies_form5.as_view() , name='gs_form5'),
    path ('create_notes_general_studies-F5/',views.CreateGeneral_Studies_Form5Notes.as_view(), name='create_gs5'),
    path('delete_notes_general_studies-F5/(?P<pk>\d+)/$', views.DeleteGeneral_Studies_Form5Notes , name='delete_gs5'),

    path('geography/form5', views.geography_form5.as_view() , name='geo_form5'),
    path ('create_notes_geography-F5/',views.CreateGeography_Form5Notes.as_view(), name='create_geo5'),
    path('delete_notes_geography-F5/(?P<pk>\d+)/$', views.DeleteGeography_Form5Notes , name='delete_geo5'),

    path('history/form5', views.history_form5.as_view() , name='his_form5'),
    path ('create_notes_history-F5/',views.CreateHistory_Form5Notes.as_view(), name='create_his5'),
    path('delete_notes_history-F5/(?P<pk>\d+)/$', views.DeleteHistory_Form5Notes , name='delete_his5'),

    path('kiswahili/form5', views.kiswahili_form5.as_view() , name='kis_form5'),
    path ('create_notes_kiswahili-F5/',views.CreateKiswahili_Form5Notes.as_view(), name='create_kis5'),
    path('delete_notes_kiswahili-F5/(?P<pk>\d+)/$', views.DeleteKiswahili_Form5Notes , name='delete_kis5'),

    path('language/form5', views.language_form5.as_view() , name='lang_form5'), 
    path ('create_notes_language-F5/',views.CreateLanguage_Form5Notes.as_view(), name='create_lang5'),
    path('delete_notes_language-F5/(?P<pk>\d+)/$', views.DeleteLanguage_Form5Notes , name='delete_lang5'),

    path('mathematics/form5', views.mathematics_form5.as_view() , name='math_form5'), 
    path ('create_notes_mathematics-F5/',views.CreateMathematics_Form5Notes.as_view(), name='create_math5'),
    path('delete_notes_mathematics-F5/(?P<pk>\d+)/$', views.DeleteMathematics_Form5Notes , name='delete_math5'),

    path('physics/form5', views.physics_form5.as_view() , name='phy_form5'),
    path ('create_notes_physics-F5/',views.CreatePhysics_Form5Notes.as_view(), name='create_phy5'),
    path('delete_notes_physics-F5/(?P<pk>\d+)/$', views.DeletePhysics_Form5Notes , name='delete_phy5'),
   
]