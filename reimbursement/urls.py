from django.urls import path

from reimbursement import views

urlpatterns = [
    path("", views.reimbursement_submission, name="reimbusement_submission"),
]
