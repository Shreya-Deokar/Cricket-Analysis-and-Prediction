from unicodedata import name
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("analysis",views.analysis,name="analysis"),
    path("player",views.player,name="player"),
    path("ParticularPlayer",views.ParticularPlayer,name="particularPlayer"),
    path("ParticularTeam",views.ParticularTeam,name="particularTeam"),
    path("ParticularYear",views.ParticularYear,name="particularYear"),
    path("ParticularGround",views.ParticularGround,name="particularGround"),
    path("DisplayGraph",views.ParticularPlayer,name="display"),
    path("GroundGraph",views.ParticularGround,name="GroundGraph"),
    path("TeamGraph",views.ParticularTeam,name="TeamGraph"),
    path("PlayerGraph",views.ParticularPlayer,name="PlayerGraph"),
    path("PredictionGraph",views.prediction1,name="PredictionGraph"),
    path("PredictGraph",views.showPredicts,name="PredictGraph"),
    path("Predictions",views.predictions,name="Predictions"),
    path("PredictionGraph1",views.prediction2,name="PredictionGraph1"),
    path("Predictions1",views.showPredicts1,name="Predictions1"),
    path("PredictionGraph2",views.prediction3,name="PredictionGraph2"),
    path("Predictions2",views.showPredicts2,name="Predictions2")
]
