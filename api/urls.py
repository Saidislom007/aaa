from django.urls import path , include

from .views import (
    GetConference,
    GetOneConference,
    GetMaqola,
    GetOneMaqola,
    GetAboutShoba,
    GetOneAboutShoba,
    GetShoba,
    GetOneShoba,
    GetWordPart,
    GetOneWordPart,
    DownloadConferenceWordFileView,

)


urlpatterns = [

    path(
        'conferences/',
        GetConference.as_view(),
        name='conference-list'
    ),

    path(
        'conferences/<int:id>/',
        GetOneConference.as_view(),
        name='conference-detail'
    ),

    path(
        'shobalar/',
        GetShoba.as_view(),
        name='shoba-list'
    ),

    path(
        'shobalar/<int:id>/',
        GetOneShoba.as_view(),
        name='shoba-detail'
    ),


    path(
        'maqolalar/',
        GetMaqola.as_view(),
        name='maqola-list'
    ),

    path(
        'maqolalar/<int:id>/',
        GetOneMaqola.as_view(),
        name='maqola-detail'
    ),


    path(
        'about-shoba/',
        GetAboutShoba.as_view(),
        name='about-shoba-list'
    ),

    path(
        'about-shoba/<int:id>/',
        GetOneAboutShoba.as_view(),
        name='about-shoba-detail'
    ),


    path(
        'word-parts/',
        GetWordPart.as_view(),
        name='word-part-list'
    ),

    path(
        'word-parts/<int:pk>/',
        GetOneWordPart.as_view(),
        name='word-part-detail'
    ),
    path('download-word-file/<int:id>/', 
         DownloadConferenceWordFileView.as_view(),
         name='download-word-file-by-id'),

]