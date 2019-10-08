from django.shortcuts import render
from  BookRead.models import *
from  BookGuan.models import *
from  django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import hashlib

from django.core.paginator import Paginator
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
            return HttpResponseRedirect('/BookGuan/login/')
    return inner
def register(request):
    if request.method == "POST":
        error_msg=""
        email=request.POST.get("email")
        password=request.POST.get("password")
        if email:
            loginuser=LoginUser.objects.filter(email=email).first()
            if not loginuser:
                user=LoginUser()
                user.email=email
                user.password=SetPassword(password)
                user.user_type=1
                user.save()
            else:
               error_msg="邮箱已经被注册，请登录"
        else:
            error_msg="邮箱不可以为空"
    return render(request, 'bookguan/register.html', locals())
def login(request):
    if request.method=="POST":
        error_msg=""
        email=request.POST.get("email")
        print(email)
        password=request.POST.get("password")
        if email:
            user=LoginUser.objects.filter(email=email).first()
            if user:
                if user.password==SetPassword(password):
                    response = HttpResponseRedirect('/BookGuan/goods_list/1/1/')
                    response.set_cookie("email",user.email)
                    response.set_cookie("userid",user.id)
                    request.session['email'] = user.email
                    return response
                else:
                    error_msg = "密码错误"
            else:
                error_msg = "用户不存在"
        else:
            error_msg = "邮箱不存在"
    return render(request, 'bookguan/login.html', locals())
@LoginVaild
def index(request):
    if request.method=="POST":
            error_msg=""
            email=request.POST.get("email")
            password=request.POST.get("password")
            if email:
                user=LoginUser.objects.filter(email=email).first()
                if user:
                    if user.password==SetPassword(password):
                        response=HttpResponseRedirect('/BookGuan/index')
                        response.set_cookie("email",user.email)
                        request.session['email']=user.email
                        return response
                    else:
                         error_msg="密码错误"
                else:
                    error_msg="用户不存在"
            else:
                error_msg="邮箱不可以为空"
    return render(request, 'bookguan/index.html', locals())
def logout(request):
    response=HttpResponseRedirect('/BookGuan/login/')
    keys=request.COOKIES.keys()
    for one in keys:
        response.delete_cookie(one)
    del request.session['username']
    return response
def base(request):
    return render(request, 'bookguan/base.html')

#表格
def goods_list(request,status,page=1):
    goods_list=Goods.objects.all()
    page = page
    if status == "0":
        goods_obj = Goods.objects.filter(goods_status=0).order_by("goods_number")
    else:
        goods_obj = Goods.objects.filter(goods_status=1).order_by("goods_number")
    goods_all = Paginator(goods_obj, 10)
    goods_list = goods_all.page(page)
    return render(request, 'bookguan/goods_list.html', locals())
    # return render(request,'vue_goods_list.html',locals())


@LoginVaild
def goods_add(request):
   goods=Goods.objects.all()
   if request.method=="POST":
        data=request.POST
        print(data)
        goods=Goods()
        goods.goods_number=data.get('goods_number')
        goods.goods_name=data.get("goods_name")
        goods.goods_author_name=data.get('goods_author_name')
        goods.goods_pro_time=data.get('goods_pro_time')
        goods.goods_content=data.get('goods_content')
        goods.goods_description=data.get('goods_description')
        goods.type_name=data.get('type_name')
        goods.picture=request.FILES.get('picture')
        goods.goods_status=1
        goods.save()
        user_id=request.COOKIES.get("userid")
        goods.goods_store=LoginUser.objects.get(id=user_id)
        goods.save()
   return render(request,"bookguan/goods_add.html",locals())
def goods_status(request,status,id):
    id=int(id)
    goods=Goods.objects.get(id=id)
    if status == "up":
        goods.goods_status = 1
    else:
        goods.goods_status = 0
    goods.save()
    url=request.META.get("HTTP_REFERER",'/BookGuan/goods_list/1/1/')
    return HttpResponseRedirect(url)

@LoginVaild
def personal_info(request):
    user_id = request.COOKIES.get("userid")
    print (user_id)
    user =LoginUser.objects.filter(id = user_id).first()
    if request.method == "POST":
        ## 获取 数据，保存数据
        data = request.POST
        print (data.get("email"))
        user.username = data.get("username")
        user.phone_number = data.get("phone_number")
        user.age = data.get("age")
        user.gender = data.get("gender")
        user.address = data.get("address")
        user.photo = request.FILES.get("photo")
        user.save()
        print (data)
    return render(request,"bookguan/personal_info.html",locals())

