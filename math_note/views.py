from time import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect
from .forms import PostForm
from datetime import datetime, timedelta
from pytz import timezone


def math_home_page(request):
    today =  datetime.now(timezone('Asia/Seoul'))
    yesterday = today - timedelta(days=1)

    model = Post.objects.all()
    todayPost = Post.objects.filter(dt_created = today)
    yesterdayPost = Post.objects.filter(dt_created = yesterday)

    return render(request, 'math_note/home.html', {'model': model, 'todayPost': todayPost, 'yesterdayPost': yesterdayPost})

def create(request):
    if request.method == 'POST':

        book = request.POST['book']
        page = request.POST['page']
        big_unit = choosing_unit(book, page, 'big')
        middle_unit = choosing_unit(book, page, 'middle')

        new_post = Post(
            book = book,
            page = page,
            number = request.POST['number'],
            WR = request.POST['WR'],
            big_unit = big_unit,
            middle_unit = middle_unit,
            image = request.FILES['image'],
        )
        new_post.save()
        return redirect('math:detail', id=new_post.id)
    else:
        note_form = PostForm
        return render(request, 'math_note/forms.html', {'form': note_form})

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'math_note/detail.html', {'post': post})


def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        post_form.save()

        return redirect('math:home-page')
    else:
        form = PostForm(instance=post)
        return render(request, 'math_note/forms.html', {'form': form})

def delete(request ,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('math:home-page')


def choosing_unit(book, page, big_or_middle):
    if book == '개념책' or book == '개념책/예제' or book == '실전책':
        if big_or_middle == 'big':
            return choosing_big_unit(book, page)
        elif big_or_middle == 'middle':
            return choosing_middle_unit(book, page)
def choosing_big_unit(book, page):
    page = int(page)
    if book == '개념책' or book == '개념책/예제':
        if page <= 7:
            return '설명'
        elif page <= 31:
            return '소인수분해'
        elif page <= 71:
            return '정수와 유리수'
        elif page <= 117:
            return '문자와 식'
        else:
            return '좌표평면과 그래프'
    elif book == 'm포스(상)/좌표평면과 그래프':
        return '좌표평면과 그래프'
    else:
        if page <= 39:
            return '소단원 실전 테스트'
        elif page <= 63:
            return '중단원 실전 테스트'
        else:
            return '중단원 서술형 대비'
def choosing_middle_unit(book, page):
    page = int(page)
    if book == '개념책' or book == '개념책/예제':
        if page <= 31 or 117 < page:
            return   choosing_big_unit(book, page)
        else:
            if page <= 49:
                return '정수와 유리수'
            elif page <= 71:
                return '정수와 유리수의 계산'
            elif page <= 97:
                return '문자의 사용과 식의 계산'
            else:
                return '일차방정식'
    elif book == 'm포스(상)/좌표평면과 그래프':
            return '좌표평면과 그래프'
    else:
        if page < 4:
            return '설명'
        elif page < 10 or (40 <= page and page < 44) or (64 <= page and page < 68):
            return '소인수분해'
        elif page < 18 or (44 <= page or page < 52) or (68<= page or page < 76):
            return '정수와 유리수'
        elif page < 32 or (52 <= page or page < 60) or (76 <= page or page < 84):
            return '문자와 식'
        else:
            return '좌표평면과 그래프'