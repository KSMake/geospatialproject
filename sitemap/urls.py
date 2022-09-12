from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

# from sitemap import views as map_views

urlpatterns = [
                  path('', Index.as_view(), name='index'),
                  path('map/', map, name='map'),
                  path('Syrdarya/', Syrdarya, name='Syrdarya'),
                  path('Balkash/', Balkash, name='Balkash'),
                  path('post/<int:pk>/', ArticleDetail.as_view(), name='post_detail'),
                  # path('add_article/', NewArticle.as_view(), name='add'),
                  path('login_registration/', login_registration, name='login_registration'),
                  path('login/', user_login, name='login'),
                  path('logout/', user_logout, name='logout'),
                  path('register/', register, name='register'),
                  path('Syrdarya/', Syrdarya, name='Syrdarya'),
                  path('Balkash/', Balkash, name='Balkash'),
                  path('Ertis/', Ertis, name='Ertis'),
                  path('Esil/', Esil, name='Esil'),
                  path('Nura/', Nura, name='Nura'),
                  path('Tobol/', Tobol, name='Tobol'),
                  path('Shu/', Shu, name='Shu'),
                  path('Zhayk/', Zhayk, name='Zhayk'),
                  path('Res/', Res, name='Res'),
                  path('Res2/', Res2, name='Res2'),
                  path('1/', Toktgul_1, name='1'),
                  path('2/', Toktgul_2, name='2'),
                  path('3/', Bahri_3, name='3'),
                  path('4/', Bahri_4, name='4'),
                  path('5/', Andizhan_5, name='5'),
                  path('6/', Andizhan_6, name='6'),
                  path('7/', Andizhan_7, name='7'),
                  path('8/', Andizhan_8, name='8'),
                  path('9/', Andizhan_9, name='9'),
                  path('10/', Andizhan_10, name='10'),
                  path('Barrace Dostyk/', Dostyk, name='Barrace Dostyk'),

                  # path('post/<int:pk>/update/', ArticleUpdate.as_view(), name='post_update'),
                  # path('post/<int:pk>/delete/', ArticleDelete.as_view(), name='post_delete'),
                  path('profile/<int:user_id>', profile, name='profile'),
                  path('search/', SearchResults.as_view(), name='search_results'),
                  # path('add_comment/<int:article_id>/', add_comment, name='add_comment')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
