from django.urls import path

from .views import CreateUpdateScoreView, ContentListView

urlpatterns = [
    path('vote/', CreateUpdateScoreView.as_view(), name='vote'),
    path('list/', ContentListView.as_view(), name='list'),
]