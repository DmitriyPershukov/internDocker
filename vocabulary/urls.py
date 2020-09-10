from django.urls import path

import vocabulary.views as views

urlpatterns = [
    path('categories', views.CategoriesView.as_view(), name='categories'),
    path('levels', views.LevelsView.as_view(), name='levels'),
    path('themes', views.ThemesView.as_view(), name='themes'),
    path('themes/<int:id>/', views.ThemesView.as_view(), name='themes'),
    path('words/<int:id>/', views.WordView.as_view(), name='words')
]