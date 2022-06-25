from django.urls import path
from myapp import views
app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.details, name='details'),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('search_results/', views.search, name='search'),
    path('fantasy/', views.fantasy, name='fantasy'),
    path('comedy/', views.comedy, name='comedy'),
    path('Finance/', views.Finance, name='Finance'),
    path('Horror/', views.Horror, name='Horror'),

]
