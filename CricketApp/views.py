from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.pyplot import get
from matplotlib.style import context
from tenacity import retry
from CricketApp.process import team
from .process.team import *
from CricketApp.process import player
from .process.player import *
from CricketApp.process import yearWise
from .process.yearWise import *
from CricketApp.process import groundWise
from .process.groundWise import *
from CricketApp.process import teamWise
from .process.teamWise import *
from CricketApp.process import playerWise
from .process.playerWise import *
from CricketApp.process import prediction
from .process.prediction import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def predictions(request):
    return render(request,"banner.html")

def prediction1(request):
    team1 = prediction.team1Name()
    team2 = prediction.team2Name()
    tossWinn = prediction.tossName()
    context={"graph1":team1,"graph2":team2,"graph3":tossWinn}
    return render(request,"prediction.html",context)

def prediction2(request):
    team1 = prediction.team1Name()
    team2 = prediction.team2Name()
    venue = prediction.venueName()
    context={"graph1":team1,"graph2":team2,"graph3":venue}
    return render(request,"prediction1.html",context)

def prediction3(request):
    team = prediction.tossName()
    context={"graph1":team}
    return render(request,"prediction2.html",context)

def showPredicts(request):
    if request.method=='POST':
        team1 = request.POST.get('team1')
        team2 = request.POST.get('team2')
        tossWin = request.POST.get('toss')
        graph1 = prediction.predict_winner(team1,team2,tossWin)
        context={"graph1":graph1}
        return render(request,"PredictGraph.html",context)
    
    return render(request,"prediction.html")

def showPredicts1(request):
    if request.method=='POST':
        team1 = request.POST.get('team1')
        team2 = request.POST.get('team2')
        venue = request.POST.get('venue')
        graph1 = prediction.predict_venue(team1,team2,venue)
        context={"graph1":graph1}
        return render(request,"PredictGraph.html",context)
    
    return render(request,"prediction1.html")

def showPredicts2(request):
    if request.method=='POST':
        team = request.POST.get('team')
        graph1 = prediction.predict_decision(team)
        context={"graph1":graph1}
        return render(request,"PredictGraph.html",context)
    
    return render(request,"prediction2.html")


def analysis(request):
    graph1 = won_by_wickets()
    Teams=team_name()
    graph2=won_by_superover()
    graph3=won_by_runs()
    graph4=total_matches()
    graph5=most_win()
    graph6=matches_per_season()
    graph7=total_run()
    graph8=no_of_times_team_won_toss()
    graph9=played_win_WinPercentage()
    graph10=toss_desicion()
    graph11=no_of_toss_wins()
    player=player_name()
    context={"graph1":graph1,"graph2":graph2,"graph3":graph3,"graph4":graph4,"graph5":graph5,
    "graph6":graph6,"graph7":graph7,"graph8":graph8,"graph9":graph9,"graph10":graph10,
    "graph11":graph11,"team":Teams,"balls":player}
    return render(request,'analysis.html',context)

def player(request):
    graph1=top_five_players()
    graph2=most_player_of_match()
    graph3=highest_run_scoring_player()
    graph4=top_bowlers()
    graph5=top_batsman()
    graph6=century()
    graph7=half_century()
    context={"graph1":graph1,"graph2":graph2,"graph3":graph3,"graph4":graph4,"graph5":graph5,
    "graph6":graph6,"graph7":graph7}
    return render(request,'allPlayer.html',context)

def ParticularYear(request):
    if request.method=='POST':
        year = request.POST.get('year')
        batsman = request.POST.get('batsman')
        bowler = request.POST.get('bowler')
        
        if request.POST.get('all'):
            graph1 = player_runs(batsman,year)
            graph2 = player_wickets(bowler,year)
            graph3 = strike_rate(batsman,year)
            graph4 = total_match(year)
            graph5 = team_won(year)
            graph6 = team_loss(year)
            graph7 = toss_won(year)
            #graph8 = toss_loss(year)
            context = {"graph1":graph1,"graph2":graph2,"graph3":graph3,"graph4":graph4,"graph5":graph5,"graph6":graph6,"graph7":graph7}
            return render(request,'YearGraph.html',context)

        if request.POST.get('graph1'):
            graph1 = player_runs(batsman,year)
            context = {"graph1":graph1}
            return render(request,'YearGraph.html',context)

        if request.POST.get('graph2'):
            graph2 = player_wickets(bowler,year)
            context = {"graph1":graph2}
            return render(request,'YearGraph.html',context)

        if request.POST.get('graph3'):
            graph3 = strike_rate(batsman,year)
            context = {"graph1":graph3}
            return render(request,'YearGraph.html',context)

        if request.POST.get('graph4'):
            graph4 = total_match(year)
            context = {"graph1":graph4}
            return render(request,'YearGraph.html',context)

        if request.POST.get('graph5'):
            graph5 = team_won(year)
            context = {"graph1":graph5}
            return render(request,'YearGraph.html',context)

        if request.POST.get('graph6'):
            graph6 = team_loss(year)
            context = {"graph1":graph6}
            return render(request,'YearGraph.html',context)

        if request.POST.get('graph7'):
            graph7 = toss_won(year)
            context = {"graph1":graph7}
            return render(request,'YearGraph.html',context)

        if request.POST.get('graph8'):
            graph8 = toss_loss(year)
            context = {"graph1":graph8}
            return render(request,'YearGraph.html',context)


    return render(request,'particularYear.html')

def ParticularTeam(request):

    if request.method=='POST':
        team = request.POST.get('team')
        year = request.POST.get('year')
        batsman = request.POST.get('batsman')
        bowler = request.POST.get('bowler')
        if request.POST.get('all'):
            graph1 = teamWise.team_match(team)
            graph2 = teamWise.venue_match(team)
            graph3 = teamWise.year_match(team)
            context = {"graph1":graph1,"graph2":graph2,"graph3":graph3}
            return render(request,"teamsGraph.html",context)
        
        if request.POST.get('graph2'):
           graph1 = teamWise.team_match(team)
           context = {"graph1":graph1}
           return render(request,"teamsGraph.html",context)
        
        if request.POST.get('graph3'):
           graph2 = teamWise.venue_match(team)
           context = {"graph1":graph2}
           return render(request,"teamsGraph.html",context)
        
        if request.POST.get('graph4'):
           graph3 = teamWise.year_match(team)
           context = {"graph1":graph3}
           return render(request,"teamsGraph.html",context)

    return render(request,'particularTeam.html')

def ParticularPlayer(request):
    if request.method=='POST':

        year = request.POST.get('year')
        batsman = request.POST.get('batsman')
        bowler = request.POST.get('bowler')

        if request.POST.get('all'):
            graph1 = playerWise.strike_rate1(batsman)
            graph2 = playerWise.strike_rate2(batsman,bowler)
            graph3 = playerWise.strike_rate3(year,batsman)
            graph4 = playerWise.player_runs(batsman,year)
            graph5 = playerWise.player_wickets(bowler,year)
            context = {"graph1":graph1,"graph2":graph2,"graph3":graph3,"graph4":graph4,"graph5":graph5}
            return render(request,"playerGraph.html",context)

        if request.POST.get('graph'):
            graph1 = playerWise.strike_rate1(batsman)
            context = {"graph1":graph1}
            return render(request,"playerGraph.html",context)

        elif request.POST.get('graph1'):
            graph2 = playerWise.strike_rate2(batsman,bowler)
            context = {"graph2":graph2}
            return render(request,"playerGraph.html",context)

        elif request.POST.get('graph2'):
            graph3 = playerWise.strike_rate3(year,batsman)
            context = {"graph3":graph3}
            return render(request,"playerGraph.html",context)

        elif request.POST.get('graph3'):
            graph4 = playerWise.player_runs(batsman,year)
            context = {"graph4":graph4}
        
            return render(request,"playerGraph.html",context)
            
        elif request.POST.get('graph4'):
            graph5 = playerWise.player_wickets(bowler,year)
            context = {"graph5":graph5}
            return render(request,"playerGraph.html",context)

    return render(request,"particularPlayer.html")

def ParticularGround(request):

    if request.method=='POST':
        venue = request.POST.get('venue')
        year = request.POST.get('year')
        batsman = request.POST.get('batsman')
        bowler = request.POST.get('bowler')

        if request.POST.get("all"):
            graph1 = groundWise.total_match(venue)
            graph2 = venue_won(venue)
            graph3 = venue_loss(venue)
            graph4 = groundWise.toss_won(venue)
            graph5 = groundWise.toss_loss(venue)
            context = {"graph1":graph1,"graph2":graph2,"graph3":graph3,"graph4":graph4,"graph5":graph5}
            return render(request,"GroundGraph.html",context)
        
        if request.POST.get("graph1"):
            graph1 = groundWise.total_match(venue)
            context = {"graph1":graph1}
            return render(request,"GroundGraph.html",context)

        if request.POST.get("graph2"):
            graph2 = venue_won(venue)
            context = {"graph2":graph2}
            return render(request,"GroundGraph.html",context)

        if request.POST.get("graph3"):
            graph3 = venue_loss(venue)
            context = {"graph3":graph3}
            return render(request,"GroundGraph.html",context)

        if request.POST.get("graph4"):
            graph4 = groundWise.toss_won(venue)
            context = {"graph4":graph4}
            return render(request,"GroundGraph.html",context)

        if request.POST.get("graph5"):
            graph5 = groundWise.toss_loss(venue)
            context = {"graph5":graph5}
            return render(request,"GroundGraph.html",context)

    return render(request,"particularGround.html")