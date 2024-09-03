import json
from logging import log
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from pytest import console_main
from django.views.decorators.csrf import csrf_exempt
from .models import Admin, User,PicTest,QuestionTest
# 表单
# def loginPage(request):
#     return render(request,'login.html')

#注册跳转
# def registerPage(request):
#     return render(request, 'register.html')


def trans(ordata):
    if ordata=='yes':
        return '是'
    elif ordata=='no':
        return '否'
    else:
        return ordata



#用户/管理员登录
def login(request):
    # id = request.GET.get('id', '')
    # password = request.GET.get('password', '')
    if request.method == 'POST':
        id = request.POST.get("id")
        password = request.POST.get("password")
        role = request.POST.get("user-type")
        
        if role == 'admin':
            #成功
            if Admin.objects.filter(id=id,password=password).exists():
                # return render(request, 'admin_func.html',locals())
                request.session['Adminid']=id
                return redirect('adminFunc')
            else:   
                messages.error(request, '账号或密码错误！')
                    # return render(request, 'login.html',locals())
                
        elif role == 'user':
             #成功
            if User.objects.filter(id=id,password=password).exists():
                user=get_object_or_404(User,id=id)
                # name=user.name
                request.session['reid']=id
                return redirect('userFunc')
                # return render(request, 'user_func.html',locals())
            else:   
                messages.error(request, '账号或密码错误！')
        return render(request, 'login.html',locals())
    return render(request, 'login.html',locals())




#用户注册
def register(request):
    if request.method == 'POST':
        reid = request.POST.get("re_id")
        repassword = request.POST.get("re_password")
        confpassword=request.POST.get("confirmPassword")
        # role = request.POST.get("reuser-type")
        
        # id = request.POST("re_id")
        # password = request.POST("re_password")
        # role = request.POST("reuser-type")

        if repassword!=confpassword:
            messages.error(request, '两次输入密码不同！')
            return redirect('registerPage')
     
        # if role == 'admin':
        #     if Admin.objects.filter(id=reid).exists():
        #         messages.error(request, '管理员账号已存在！')
        #         return render(request, 'register.html')
        #     else:
        #         admin = Admin.objects.create(id=reid, password=repassword)
        #         admin.save()
        #         messages.error(request, '注册成功，请登录。')
        #         return redirect('loginPage')
        # elif role == 'user':

        if User.objects.filter(id=reid).exists():
            messages.error(request, '用户账号已存在！')
            return render(request, 'register.html')
        else:
            user = User.objects.create(id=reid, password=repassword)
            user.save()     
                # messages.error(request, '注册成功，请完善信息。')

            request.session['reid']=reid
            return redirect('infoColl')    
    return render(request, 'register.html')


#用户注册信息收集
def infoColl(request):
    reid=request.session.get('reid')
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        birth=request.POST.get('birthdate')
        education=request.POST.get('education')
        gender=request.POST.get("gender")
        if gender=='male':
            gender='男'
        elif gender=='female':
            gender='女'
        exercise=request.POST.get('exercise')
        readnwrite=request.POST.get('reading_writing')
        sleeping=request.POST.get('sleeping')
        smoking=request.POST.get('smoking')
        smoking=trans(smoking)
        diet=request.POST.get('diet')
        diet=trans(diet)
        living=request.POST.get('living')
        working=request.POST.get('working')
        ADhistory=request.POST.get('ADhistory')
        ADhistory=trans(ADhistory)
        disease=request.POST.get('disease')
        disease=trans(disease)
        TBI=request.POST.get('TBI')
        TBI=trans(TBI)

        user=get_object_or_404(User,id=reid)
        user.name=name
        user.phonenumber=phone
        user.age=birth
        user.education=education
        user.gender=gender
        user.workout=exercise
        user.readnwrite=readnwrite
        user.sleeping=sleeping
        user.smoking=smoking
        user.diet=diet
        user.living=living
        user.working=working
        user.ADhistory=ADhistory
        user.disease=disease
        user.TBI=TBI
        user.save()
        request.session['reid']=reid

        return redirect('userFunc')
        # return render(request,'user_func.html',locals())
    return render(request,'info_coll.html',locals())
    # redirect('loginPage')



#看图描述
@csrf_exempt  # 临时禁用 CSRF 保护（仅用于测试，生产环境中应启用）
def userFunc(request):
    id=request.session.get('reid')
    if request.method == 'POST':
        test_date = request.POST.get('testDate')
        audio_file = request.FILES.get('audio')

        if not test_date:
            return JsonResponse({'status': 'error', 'message': '缺少测试日期'}, status=400)
        if not audio_file:
            return JsonResponse({'status': 'error', 'message': '缺少音频文件'}, status=400)

        try:
            # 读取文件内容为二进制数据
            audio_data = audio_file.read()
            

            #重复提交
            if PicTest.objects.filter(testId=id,testDate=test_date,audio=audio_data).exists():
                return JsonResponse({'status': 'error', 'message': '请勿重复提交相同录音！'}, status=500)

            # 保存到数据库
            picTest = PicTest.objects.create(testId=id,testDate=test_date, audio=audio_data)
            picTest.save()

            return JsonResponse({'status': 'success', 'message': '录音提交成功!'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return render(request, 'user_func.html', locals())


#MMSE问卷测试
def question(request):
    id=request.session.get('reid')
    if request.method == 'POST':
        test_date = request.POST.get('testdate')
        date_score=request.POST.get('date_score')
        place_score=request.POST.get('place_score')
        registration_score=request.POST.get('registration_score')
        attention_calculation_score=request.POST.get('attention_calculation_score')
        recall_score=request.POST.get('recall_score')
        language_score=request.POST.get('language_score')
        repeat_score=request.POST.get('repeat_score')
        command_score=request.POST.get('command_score')
        reading_score=request.POST.get('reading_score')
        writing_score=request.POST.get('writing_score')
        drawing_score=request.POST.get('drawing_score')
        notes=request.POST.get('drawing_detail')
        audio_file = request.FILES.get('audio')
        # print(f"Place Score: {place_score}")
        # print(request.POST)

        if not test_date:
            return JsonResponse({'status': 'error', 'message': '缺少测试日期'}, status=400)
        if not audio_file:
            return JsonResponse({'status': 'error', 'message': '缺少音频文件'}, status=400)

        try:
            # 读取文件内容为二进制数据
            audio_data = audio_file.read()
            #重复提交
            if QuestionTest.objects.filter(testId=id,testDate=test_date,audio=audio_data).exists():
                return JsonResponse({'status': 'error', 'message': '请勿重复提交相同录音！'}, status=500)

            # 保存到数据库
            questionTest = QuestionTest.objects.create(testId=id,testDate=test_date,todayDate=date_score,
                                      position=place_score,remember=registration_score,
                                      calculate=attention_calculation_score,
                                      memorize=recall_score,named=language_score,
                                      repeating=repeat_score,commandOperate=command_score,
                                      wordOperate=reading_score,writing=writing_score,
                                      draw=drawing_score,notes=notes,audio=audio_data)
            questionTest.save()
            # return JsonResponse({'status': 'success', 'message': date_score}, status=200)
            return JsonResponse({'status': 'success', 'message': '录音和问卷结果提交成功!'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return render(request,'questionMMSE.html',locals())



#个人信息修改
def mine(request):
    id=request.session.get('reid')
    user=get_object_or_404(User,id=id)
    name=user.name
    gender=user.gender
    if user.gender=='male':
        gender='男'
    elif user.gender=='female':
        gender='女'
    # else:
    #     gender='未选择'
    birth=user.age
    phone=user.phonenumber
    education=user.education
    exercise=user.workout
    readnwrite=user.readnwrite
    sleeping=user.sleeping
    # sleeping=trans(sleeping)
    # smoking=user.smoking
    smoking=trans(user.smoking)
    diet=user.diet
    diet=trans(diet)
    living=user.living
    working=user.working
    ADhistory=user.ADhistory
    ADhistory=trans(ADhistory)
    disease=user.disease
    disease=trans(disease)
    TBI=user.TBI
    TBI=trans(TBI)
    # picTest=[]
    test_date_l=[]
    picTest=PicTest.objects.filter(testId=id)
    for i in picTest:
        test_date_l.append(i.testDate)


    test_date_l2=[]
    questionTest=QuestionTest.objects.filter(testId=id)
    for i in questionTest:
        test_date_l2.append(i.testDate)
    # print(f"测试: {test_date_l2}")

    #修改信息更新数据库
    if request.method=='POST':
        nameE=request.POST.get('username')
        genderE=request.POST.get('gender')
        # genderE=request.POST.get('gender')
        # if request.POST.get('gender')=='男':
        #     gender='male'
        # elif request.POST.get('gender')=='女':
        #     gender='female'
        birthE=request.POST.get('birthdate')
        phoneE=request.POST.get('phone')
        educationE=request.POST.get('education')
        exerciseE=request.POST.get('exercise')
        readnwriteE=request.POST.get('reading_writing')
        sleepingE=request.POST.get('sleeping')
        # smokingE=request.POST.get('smoking')
        smokingE=trans(request.POST.get('smoking'))
        # print(f"测试: {smokingE}")
        dietE=request.POST.get('diet')
        dietE=trans(dietE)
        livingE=request.POST.get('living')
        workingE=request.POST.get('working')
        ADhistoryE=request.POST.get('ADhistory')
        ADhistoryE=trans(ADhistoryE)
        diseaseE=request.POST.get('disease')
        diseaseE=trans(diseaseE)
        TBIE=request.POST.get('TBI')
        TBIE=trans(TBIE)
        # if phoneE.length!=11:
        #     return JsonResponse({'status': 'error', 'message': '手机号位数不正确!'}, status=500)
        user.name=nameE
        user.gender=genderE
        user.age=birthE
        user.phonenumber=phoneE
        user.education=educationE
        user.workout=exerciseE
        user.readnwrite=readnwriteE
        user.sleeping=sleepingE
        user.smoking=smokingE
        user.diet=dietE
        user.living=livingE
        user.working=workingE
        user.ADhistory=ADhistoryE
        user.disease=diseaseE
        user.TBI=TBIE
        user.save()
        return redirect('mine')

    return render(request,'mine.html',locals())


#用户密码修改
def user_psw(request):
    id=request.session.get('reid')
    user=get_object_or_404(User,id=id)
    pwd=user.password
    # print(f"测试: {pwd}")

    if request.method=='POST':
        orpwd=request.POST.get('orpassword')
        repwd=request.POST.get('re_password')
        conpwd=request.POST.get('confirm_password')
        # print(f"测试1: {orpwd}")
        # print(f"测试2: {repwd}")
        if not orpwd or not repwd or not conpwd:
            messages.error(request, '所有字段都是必填的!')
            return redirect('user_psw')
        if repwd!=conpwd:
            messages.error(request, '两次输入密码不同！')
            return redirect('user_psw')
        if pwd!=orpwd:
            messages.error(request, '原始密码不正确！')
            return redirect('user_psw')
        
        

        user.password=repwd
        user.save()
        # messages.error(request, '修改成功!')
        return redirect('mine')
        # return JsonResponse({'status': 'success', 'message': '修改成功!'}, status=200)

    return render(request,'user_psw.html',locals())






#管理员密码修改
def adminEdit(request):
    id=request.session.get('Adminid')
    print(f"TEST: {id}")
    admin=get_object_or_404(Admin,id=id)
    pwd=admin.password
    # print(f"测试: {pwd}")

    if request.method=='POST':
        orpwd=request.POST.get('orpassword')
        repwd=request.POST.get('re_password')
        conpwd=request.POST.get('confirm_password')
        # print(f"测试1: {orpwd}")
        # print(f"测试2: {repwd}")
        if not orpwd or not repwd or not conpwd:
            messages.error(request, '所有字段都是必填的!')
            return redirect('adminEdit')
        if repwd!=conpwd:
            messages.error(request, '两次输入密码不同！')
            return redirect('adminEdit')
        if pwd!=orpwd:
            messages.error(request, '原始密码不正确！')
            return redirect('adminEdit')
        
        

        admin.password=repwd
        admin.save()
        # messages.error(request, '修改成功!')
        return redirect('adminFunc')
        # return JsonResponse({'status': 'success', 'message': '修改成功!'}, status=200)

    return render(request,'admin_edit.html',locals())



#重置密码
def user_reset(request,user_id):
    print(f"测试1: {id}")
    user = get_object_or_404(User, id=user_id)
    user.password = '11111111'  
    user.save()
    messages.success(request, f'已将用户 {user.name} 的密码重置为 11111111')
    return redirect('adminFunc')  # 重定向到管理员页面



#管理员搜索功能（查）
#搜索也可以了,!!!考虑要不要改模糊搜索
def adminFunc(request):
    id=request.session.get('Adminid')
    print(f"TEST1: {id}")
    # users = User.objects.all()
    query = request.GET.get('q')
    
    if query:
        users = User.objects.filter(name=query)
    else:
        users = User.objects.all()

    # 上传用户信息账号是否存在
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('username')
        # user_id=request.POST.get['userID']
        user_exists = User.objects.filter(id=user_id).exists()

        return JsonResponse({'exists': user_exists})
    # if request.method=='POST':
    #     user_id=request.POST.get['userID']
    #     if not User.objects.filter(id=user_id).exists():
    #         messages.error(request, '用户账号不存在！')
    #         redirect('adminFunc')
    #     else:
    #         return render(request,'upload_user_info.html',locals())

    return render(request,'admin_func.html',locals())



#管理员功能（改）
#修改用户信息，重置密码
def user_edit(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        user.name = request.POST.get('name')
        user.gender = request.POST.get('gender')
        user.age = request.POST.get('birthdate')
        user.phonenumber = request.POST.get('phonenumber')
        user.education = request.POST.get('education')
        user.workout = request.POST.get('exercise')
        user.readnwrite = request.POST.get('reading_writing')
        user.sleeping = request.POST.get('sleeping')
        user.smoking = request.POST.get('smoking')
        user.diet = request.POST.get('diet')
        user.living = request.POST.get('living')
        user.working = request.POST.get('working')
        user.ADhistory = request.POST.get('ADhistory')
        user.disease = request.POST.get('disease')
        user.TBI = request.POST.get('TBI')
        user.save()
        messages.success(request, '用户信息已更新')
        return redirect('adminFunc')  # 重定向到用户列表页面
    return redirect('adminFunc')



#管理员功能（删）
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    picTest=PicTest.objects.filter(testId=user_id)
    for i in picTest:
        i.delete()
    questionTest=QuestionTest.objects.filter(testId=user_id)
    for j in questionTest:
        j.delete()
    return redirect('adminFunc')


#把全部信息显示出来
def user_detail(request,user_id):
    user = get_object_or_404(User, id=user_id)
    test_date=[]
    picTest=PicTest.objects.filter(testId=user_id)
    for i in picTest:
        test_date.append(i.testDate)

    test_date2=[]
    questionTest=QuestionTest.objects.filter(testId=user_id)
    for i in questionTest:
        test_date2.append(i.testDate)
    return render(request,'user_detail.html',locals())


#管理员功能（增）
def upload_user_info(request, username):
    # 在这里处理信息上传的逻辑
    request.session['id']=username
    if request.method == 'POST':
        test=request.POST.get('test_type')
        id=username
        print(f"TEST: {test}")
        if test=='test1':
            # print(f"test1111111111")
            test_date = request.POST.get('test_date')
            audio_file = request.FILES.get('audio_file')
            audio=audio_file.read()
            picTest=PicTest.objects.create(testId=id,testDate=test_date,audio=audio)
            picTest.save()
            # 处理录音文件的保存逻辑，可能将其转化为BLOB存储到数据库

            # 提交成功后，可以重定向或给出提示信息
            messages.success(request, '上传成功！')
            return redirect('upload_user_info',username=username)  # 替换为上传成功后的页面
        elif test=='test2':
            # print(f"test2222222222")
            test_date = request.POST.get('test_date2')
            audio_file = request.FILES.get('audio_file2')
            audio=audio_file.read()
            date_score=request.POST.get('date_score')
            place_score=request.POST.get('place_score')
            registration_score=request.POST.get('registration_score')
            attention_calculation_score=request.POST.get('attention_calculation_score')
            recall_score=request.POST.get('recall_score')
            language_score=request.POST.get('language_score')
            repeat_score=request.POST.get('repeat_score')
            command_score=request.POST.get('command_score')
            reading_score=request.POST.get('reading_score')
            writing_score=request.POST.get('writing_score')
            drawing_score=request.POST.get('drawing_score')
            notes=request.POST.get('drawing_detail')
            if QuestionTest.objects.filter(testId=id,testDate=test_date,audio=audio).exists():
                return JsonResponse({'status': 'error', 'message': '请勿重复提交相同录音！'}, status=500)

            # 保存到数据库
            questionTest = QuestionTest.objects.create(testId=id,testDate=test_date,todayDate=date_score,
                                      position=place_score,remember=registration_score,
                                      calculate=attention_calculation_score,
                                      memorize=recall_score,named=language_score,
                                      repeating=repeat_score,commandOperate=command_score,
                                      wordOperate=reading_score,writing=writing_score,
                                      draw=drawing_score,notes=notes,audio=audio)
            questionTest.save()
            messages.success(request, '上传成功！')
            return redirect('upload_user_info',username=username)  # 替换为上传成功后的页面
    return render(request, 'upload_user_info.html', locals())



