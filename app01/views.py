from django.shortcuts import render, HttpResponse

# Create your views here.

from rbac.models import *
from rbac.service.perssions import *


class Per(object):
    def __init__(self, actions):
        self.actions = actions
    def add(self):
        return "add" in self.actions
    def delete(self):
        return "delete" in self.actions
    def edit(self):
        return "edit" in self.actions
    def list(self):
        return "list" in self.actions


def users(request):
    user_list = User.objects.all()
    permission_list = request.session.get("permission_list")

    # 查询当前登录人的名字
    id = request.session.get("user_id")
    user = User.objects.filter(id=id).first()
    print(user)

    per = Per(request.actions)


    return render(request, "rbac/users.html", locals())


def add_user(request):
    return HttpResponse('add user')


def delete_user(request, id):
    return HttpResponse('delete_user')


def edit_user(request, id):
    return HttpResponse('edit_user')


def roles(request):
    role_list = Role.objects.all()

    per = Per(request.actions)
    print(request.actions)
    return render(request, "rbac/roles.html", locals())


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = User.objects.filter(name=user, pwd=pwd).first()
        if user:
            ############## 在session中注册用户
            request.session['user_id'] = user.pk

            ############# 在session中注册权限list
            initial_session(request, user)

            return HttpResponse("登录成功")

    return render(request, 'login.html', locals())
