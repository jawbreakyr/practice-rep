from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
	path("polls/", views.index, name="index"),
    # ex: /1/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /1/results
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /1/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
	# user requests a url which is resolved through this urls.py 
    # which thens calls the corresponding function inside the views.py 
]