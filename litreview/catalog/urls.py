from django.urls import path
from . import views


urlpatterns = [
    path("", views.feed, name="feed"),
    path("my-post/", views.my_post, name="my-post"),
    path("create-ticket/", views.TicketCreateView.as_view(), name="create-ticket"),
    path(
        "update-ticket/<int:pk>", views.TicketUpdateView.as_view(), name="update-ticket"
    ),
    path(
        "delete-ticket/<int:pk>", views.TicketDeleteView.as_view(), name="delete-ticket"
    ),
    path("ticket/<int:pk>", views.TicketDetailView.as_view(), name="ticket-detail"),
    path("create-review/", views.create_review, name="create-review"),
    path(
        "create-review/<int:pk>", views.create_review, name="create-review-from-ticket"
    ),
    path(
        "update-review/<int:pk>", views.ReviewUpdateView.as_view(), name="update-review"
    ),
    path(
        "delete-review/<int:pk>", views.ReviewDeleteView.as_view(), name="delete-review"
    ),
    path("review/<int:pk>", views.ReviewDetailView.as_view(), name="review-detail"),
]
