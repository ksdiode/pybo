from django.urls import path
from .views import index, detail
# from . import views

app_name = 'pybo'
urlpatterns = [
    path('', index, name='index'),    # config/urls.py에서 'pybo/' + '' --> 'pybo/'
    path('<int:question_id>/', detail, name='detail'),
]