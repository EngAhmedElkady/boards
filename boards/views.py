from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required
# Create your views here.



def Home(request):
    boards=Board.objects.all() 
    return render(request,'home.html',{"boards":boards})


def Board_topics(request,id):
    # try:
    #    board=Board.objects.get(id=id) 
    # except :
    #     raise Http404

    board2=get_object_or_404(Board,pk=id)
    topics=Topic.objects.filter(board=board2.id)
    return render(request,'topics.html',{"board":board2,'topics':topics})
@login_required
def new_topic(request,id):
    board2=get_object_or_404(Board,pk=id)
    # user = User.objects.first()
    user=request.user

    if request.method=='POST':
        form=Newtopicform(request.POST)
        if form.is_valid():
            topic=form.save(commit=False)
            topic.created_by=user
            topic.board=board2
            topic.save()

            Post.objects.create(
                massage=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )

            return redirect('boards',id=board2.pk)
    else:
        form = Newtopicform()

    return render(request,'new_topic.html',{"board":board2,'form':form})



def all_posts(request,id,topic_id):
    board2=get_object_or_404(Board,pk=id)
    topics=Topic.objects.get(board=board2.id,id=topic_id)
    return render(request,'all_post.html',{'topic':topics})
    