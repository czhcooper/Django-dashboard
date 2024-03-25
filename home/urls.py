from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pages/dashboard', views.dashboard, name='dashboard'),
    path('pages/pipeline/qiime2', views.pipeline_16S, name='pipeline_16S'),
    path('pages/pipeline/rnaseq', views.pipeline_rnaseq, name='pipeline_rnaseq'),
    path('pages/pipeline/rnaseq/run', views.run_analysis_rnaseq, name='pipeline_rnaseq_run'),

    path('test', views.test, name='test'),
    
]
