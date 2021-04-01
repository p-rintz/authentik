"""authentik URL Configuration"""
from django.urls import path

from authentik.admin.views import policies, sources, stages

urlpatterns = [
    # Sources
    path("sources/create/", sources.SourceCreateView.as_view(), name="source-create"),
    path(
        "sources/<uuid:pk>/update/",
        sources.SourceUpdateView.as_view(),
        name="source-update",
    ),
    # Policies
    path("policies/create/", policies.PolicyCreateView.as_view(), name="policy-create"),
    path(
        "policies/<uuid:pk>/update/",
        policies.PolicyUpdateView.as_view(),
        name="policy-update",
    ),
    # Stages
    path("stages/create/", stages.StageCreateView.as_view(), name="stage-create"),
    path(
        "stages/<uuid:pk>/update/",
        stages.StageUpdateView.as_view(),
        name="stage-update",
    ),
]
