from django.urls import path

from .views import PinList, PinDetail, UserList, \
    UserDetail, CategoryList, CategoryDetail, \
    CategoryCount, StatusList, StatusDetail, \
    CrowdfundingList, CrowdfundingDetail, ImagesList, ImagesDetail

urlpatterns = [
    path('pin/<int:pk>/', PinDetail.as_view()),
    path('pin/', PinList.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('category/count/', CategoryCount.as_view()),
    path('status/', StatusList.as_view()),
    path('status/<int:pk>/', StatusDetail.as_view()),
    path('images/', ImagesList.as_view()),
    path('images/<int:pk>/', ImagesDetail.as_view()),
    path('crowdfunding/', CrowdfundingList.as_view()),
    path('crowdfunding/<int:pk>/', CrowdfundingDetail.as_view()),
]
