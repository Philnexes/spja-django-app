from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post, Comment, Like, User, Message, Group, Group_users


def index(request):
    latest_posts_list = Post.objects.order_by('-pub_date')[:5]       
                   
    context = {'latest_posts_list': latest_posts_list}
    return render(request, 'polls/index.html', context)

def users(request):
    latest_users_list = User.objects.order_by('-nick')[:5]

    context = {'latest_users_list': latest_users_list}
    return render(request, 'polls/users.html', context)

def add(request):
    return render(request, 'polls/add.html')
    
def add_save(request):
    if request.POST['nick'] != "" and request.POST['text'] != "":
        p = Post(nick = request.POST['nick'], post_text = request.POST['text'])
        p.save()
        return HttpResponseRedirect('/polls')
    else:  
        return render(request, 'polls/add.html', {
            'error_message': "Fill nick and post text!",
        })   
    
def delete(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    p.delete()
    return HttpResponseRedirect('/polls')         
    
def like(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    l = Like(post = p)
    l.save()
    return HttpResponseRedirect('/polls')

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'polls/detail.html', {'post': post})
    
def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'polls/comment.html', {'post': post})  
    
def comment_save(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    if request.POST['nick'] != "" and request.POST['text'] != "":
        c = Comment(nick = request.POST['nick'], comment_text = request.POST['text'], post = p)
        c.save()
        return HttpResponseRedirect('/polls/' + str(p.id) + '/detail')
    else:  
        return render(request, 'polls/comment.html', {
            'post': p,
            'error_message': "Fill nick and post text!",
        })
        
def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'polls/edit.html', {'post': post})  
    
def edit_save(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    if request.POST['nick'] != "" and request.POST['text'] != "":    
        p.nick = request.POST['nick']
        p.post_text = request.POST['text']
        p.save() 
        return HttpResponseRedirect('/polls/')
    else:  
        return render(request, 'polls/edit.html', {
            'post': p,
            'error_message': "Vyplň přezdívku a komentář!",
        })                   


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question}) 

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'polls/user_detail.html', {'user': user})
def user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'polls/user_edit.html', {'user': user})
def user_edit_save(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    if request.POST['nick'] != "" and request.POST['text'] != "" and request.POST['pswd'] != "":
        u.nick = request.POST['nick']
        u.pswd = request.POST['pswd']
        u.icon = request.POST['icon']
        u.text = request.POST['text']
        u.save()
        return HttpResponseRedirect('/polls/users')
    else:
        return render(request, 'polls/user_edit.html', {
            'user': u,
            'error_message': "Vyplň přezdívku a heslo!",
        })
def user_register(request):
    return render(request, 'polls/user_register.html')
def user_register_save(request):
    if request.POST['nick'] != "" and request.POST['text'] != "" and request.POST['pswd'] != "":
        u = User(nick=request.POST['nick'], pswd=request.POST['pswd'], text=request.POST['text'], icon=request.POST['icon'])
        u.save()
        return HttpResponseRedirect('/polls/users')
    else:
        return render(request, 'polls/user_register.html', {
            'user': u,
            'error_message': "Vyplň přezdívku a heslo!",
        })


def message(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'polls/message.html', {'user': user})


def message_save(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    if request.POST['nick'] != "" and request.POST['text'] != "":
        c = Message(nick=request.POST['nick'], text=request.POST['text'], icon=request.POST['icon'], user=u)
        c.save()
        return HttpResponseRedirect('/polls/' + str(u.id) + '/user_detail')
    else:
        return render(request, 'polls/edit_message.html', {
            'user': u,
            'error_message': "Fill nick and post text!",
        })

def group_add(request):
    return render(request, 'polls/group.html')

def group_add_save(request):
    if request.POST['title'] != "" and request.POST['text'] != "":
        g= Group(title=request.POST['title'], text=request.POST['text'])
        g.save()
        return HttpResponseRedirect('/polls/groups')
    else:
        return render(request, 'polls/group_add.html', {
            'group': g,
            'error_message': "Vyplň title a text!",
        })

def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'polls/group_detail.html', {'group': group})

def group_delete(request, group_id):
    g = get_object_or_404(Group, pk=group_id)
    g.delete()
    return HttpResponseRedirect('/polls')