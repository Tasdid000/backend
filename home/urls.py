from django.urls import path
from .views import *
urlpatterns = [
    path('Contact/feedback', ContactAPIView.as_view()),
    path('JobApply/jobapply', JobapplyAPIView.as_view()),#http://127.0.0.1:8000/apiv1/JobApply/jobapply
    path('Order/order', orderAPIView.as_view()),
    path('Portfolio/', PortfolioListAPIView.as_view()),#http://127.0.0.1:8000/apiv1/Portfolio/
    path('Post/', PostListAPIView.as_view()),
    path('Job/', JobListAPIView.as_view()),
    path('Certifaction/', certificationsListAPIView.as_view()),
]
