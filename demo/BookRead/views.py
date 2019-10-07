from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect,JsonResponse
import hashlib
from BookRead.models import *
from BookGuan.models import *
from django.core.paginator import Paginator
# Create your views here.


#加密
def SetPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result
#装饰器
def LoginVaild(func):
    def inner(request,*args,**kwargs):
        email=request.COOKIES.get("email")
        print(email)
        email_session=request.session.get("email")
        print(email_session)
        if email and  email_session and email== email_session:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/BookRead/login/')
    return inner
#登入
def login(request):
    if request.method == "POST":
        error_msg = ""
        email = request.POST.get("email")
        print(email)
        password = request.POST.get("password")
        if email:
            user = LoginUser.objects.filter(email=email).first()
            if user:
                if user.password == SetPassword(password):
                    response = HttpResponseRedirect('/BookRead/index')
                    response.set_cookie("email", user.email)
                    response.set_cookie("userid", user.id)
                    request.session['email'] = user.email
                    return response
                else:
                    error_msg = "密码错误"
            else:
                error_msg = "用户不存在"
        else:
            error_msg = "邮箱不存在"
    return render(request,"bookread/login.html",locals())
#注册
def register(request):
    if request.method == "POST":
        error_msg = ""
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email:
            loginuser = LoginUser.objects.filter(email=email).first()
            if not loginuser:
                user = LoginUser()
                user.email = email
                user.password = SetPassword(password)
                user.user_type = 0
                user.save()
            else:
                error_msg = "邮箱已经被注册，请登录"
        else:
            error_msg = "邮箱不可以为空"
    return render(request,"bookread/register.html",locals())

#模版

#父类模板
def base(request):

    return render(request,"bookread/base.html",locals())

#主页
@LoginVaild
def index(request):
    #获取cookie 获取用户名
    # username= request.COOKIES.get('username')
    # print(request.COOKIES)
    # print(username)
    # if username:
    #来源
    url = request.META.get('HTTP_REFERER')
    print(url)

    article = Goods.objects.order_by('-goods_pro_time')[:6]
    recommend_acticle=Goods.objects.order_by('goods_pro_time').all()[:7]

    click_article = Goods.objects.order_by('-goods_pro_time')[:12]

    # else:
    #     return HttpResponseRedirect('/login/')
    return render(request, 'bookread/index.html', locals())

def listpic(request):

    return render(request,'bookread/listpic.html',locals())

@LoginVaild
def newslistpic(request,page=1):
    page=int(page)
    article=Goods.objects.order_by('-goods_pro_time')

    paginator = Paginator(article,6)#每页6个
    page_obj = paginator.page(page)

    #获取当前页
    current_page = page_obj.number
    start = current_page - 3
    if start < 1:
        start=0
    end = current_page + 2
    if end > paginator.num_pages:
        end = paginator.num_pages
    if start == 0:
        end = 5
    if end == 17:
        start=12
    page_range = paginator.page_range[start:end]
    return render(request,'bookread/newslistpic.html',locals())

def about(request):

    return render(request,'bookread/about.html',locals())
@LoginVaild
def xiangxi(request,id):
    article=Goods.objects.get(id=int(id))
    return render(request,'bookread/xiangxi.html',locals())