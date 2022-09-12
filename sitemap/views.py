from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Category, Post, Comment
# Create your views here.
from .models import Search
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.db.models import Q
import folium
from folium.plugins import Fullscreen
import os
import geocoder
from .forms import SearchFrom


# Create your views here.
class Index(ListView):  # index.html
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'
    extra_context = {
        'title': 'Главная страница'
    }


def Balkash(request):
    posts = Post.objects.all()
    context = {
        'title': 'Balkash',
        'posts': posts,
    }
    return render(request, 'Balkash.html', context)


def map(request):
    if request.method == 'POST':
        form = SearchFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = SearchFrom()

    address = Search.objects.all()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country

    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')
    m = folium.Map(location=[48.019573, 66.923683], tiles="OpenStreetMap", zoom_start=5, control_scale=True)
    style_basin = {'fillColor': 'orangered'}
    style_river = {'color': 'slateblue'}

    folium.GeoJson(os.path.join(shp_dir, 'basin.geojson'), name='Границы бассейнов',
                   style_function=lambda feature: {
                       'color': 'ForestGreen',
                       'weight': 3},
                   highlight_function=lambda feature: {
                       'color': '#000000',
                       'fillOpacity': 0.50,
                       'weight': 0.1
                   }).add_to(m)
    folium.GeoJson(os.path.join(shp_dir, 'rivers.geojson'), name='Реки',
                   style_function=lambda feature: {
                       'color': 'dodgerblue',
                       'weight': 3},
                   highlight_function=lambda feature: {
                       'color': '#000000',
                       'fillOpacity': 0.50,
                       'weight': 0.1
                   }).add_to(m)

    folium.GeoJson(os.path.join(shp_dir, 'side_inflow.geojson'), name='Боковой приток',
                   style_function=lambda feature: {
                       'color': 'PaleVioletRed',
                       'weight': 3},
                   highlight_function=lambda feature: {
                       'color': '#000000',
                       'fillOpacity': 0.50,
                       'weight': 0.1}).add_to(m)

    folium.LayerControl().add_to(m)
    Fullscreen(title="Полноэкранный режим", title_cancel="Выйти из полноэкранного режима").add_to(m)
    m = m._repr_html_()

    context = {'m': m,
               'form': form,
               }
    return render(request, 'map.html', context)


def Syrdarya(request):
    posts = Post.objects.all()
    context = {
        'title': 'Syrdarya',
        'posts': posts,
    }
    return render(request, 'Syrdarya.html', context)


def Ertis(request):
    posts = Post.objects.all()
    context = {
        'title': 'Ertis',
        'posts': posts,
    }
    return render(request, 'Ertis.html', context)


def Esil(request):
    posts = Post.objects.all()
    context = {
        'title': 'Esil',
        'posts': posts,
    }
    return render(request, 'Esil.html', context)


def Nura(request):
    posts = Post.objects.all()
    context = {
        'title': 'Nura',
        'posts': posts,
    }
    return render(request, 'Nura.html', context)


def Tobol(request):
    posts = Post.objects.all()
    context = {
        'title': 'Tobol',
        'posts': posts,
    }
    return render(request, 'Tobol.html', context)


def Shu(request):
    posts = Post.objects.all()
    context = {
        'title': ' Shu',
        'posts': posts,
    }
    return render(request, 'Shu.html', context)


def Zhayk(request):
    posts = Post.objects.all()
    context = {
        'title': 'Zhayk',
        'posts': posts,
    }
    return render(request, 'Zhayk.html', context)


def Res(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилища',
        'posts': posts,
    }
    return render(request, 'Res.html', context)

def Res2(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилища',
        'posts': posts,
    }
    return render(request, 'Res2.html', context)

def Toktgul_1(request):
    posts = Post.objects.all()
    context = {
        'title': 'Токтогульское водохранилище',
        'posts': posts,
    }
    return render(request, '1.html', context)


def Toktgul_2(request):
    posts = Post.objects.all()
    context = {
        'title': 'Токтогульское водохранилище',
        'posts': posts,
    }
    return render(request, '2.html', context)


def Bahri_3(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилище Бахри Точик',
        'posts': posts,
    }
    return render(request, '3.html', context)


def Bahri_4(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилище Бахри Точик',
        'posts': posts,
    }
    return render(request, '4.html', context)


def Andizhan_5(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилище Андижанское',
        'posts': posts,
    }
    return render(request, '5.html', context)


def Andizhan_6(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилище Андижанское',
        'posts': posts,
    }
    return render(request, '6.html', context)


def Andizhan_7(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилище Чарвакское',
        'posts': posts,
    }
    return render(request, '7.html', context)


def Andizhan_8(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилище Чарвакское',
        'posts': posts,
    }
    return render(request, '8.html', context)


def Andizhan_9(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилище Шардаринское',
        'posts': posts,
    }
    return render(request, '9.html', context)


def Andizhan_10(request):
    posts = Post.objects.all()
    context = {
        'title': 'Водохранилище Шардаринское',
        'posts': posts,
    }
    return render(request, '10.html', context)


class ArticleByCategory(Index):
    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context


class ArticleDetail(DetailView):  # article_detail.html
    model = Post
    template_name = 'article_detail.html'

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])


def get_context_data(self, **kwargs):
    context = super().get_context_data()
    article = Post.objects.get(pk=self.kwargs['pk'])
    article.watched += 1
    article.save()
    context['title'] = f'Статья: {article.title}'
    context['comments'] = Comment.objects.filter(post=article)
    posts = Post.objects.all()
    posts = posts.order_by('-watched')[:4]

    context['posts'] = posts

    if self.request.user.is_authenticated:
        context['comment_form'] = CommentForm()

    return context

    # class NewArticle(CreateView):
    # form_class = PostForm
    # template_name = 'article_form.html'
    # extra_context = {
    #    'title': 'Добавить статью'
    # }

    # class ArticleUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'article_form.html'


class ArticleDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('index')
    context_object_name = 'post'


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    articles = Post.objects.filter(author=user)
    context = {
        'user': user,
        'articles': articles
    }

    return render(request, 'profile.html', context)


class SearchResults(Index):
    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = Post.objects.filter(
            Q(title__icontains=word) | Q(content__icontains=word)
        )
        return articles


def login_registration(request):
    context = {
        'title': 'Войти или зарегестрироваться',
        'login_form': LoginForm(),
        'registration_form': RegistrationForm()

    }
    return render(request, 'login_registration.html', context)


def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')
    else:
        messages.error(request, 'Не верное имя пользователя или пароль')
        return redirect('login_registration')


def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    form = RegistrationForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        messages.success(request, 'Аккаунт успешно создан. Войдите в аккаунт')
    else:
        messages.error(request, )
    return redirect('login_registration')


def Dostyk(request):
    posts = Post.objects.all()
    context = {
        'title': 'Канал Достык',
        'posts': posts,
    }
    return render(request, 'Barrace Dostyk.html', context)
