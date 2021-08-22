from collections import namedtuple
from os import name
from django.contrib.auth.models import AnonymousUser
from django.urls import path
from django.utils.timezone import activate
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('',main_view,name='main'),
    # path('signup/',signup,name='signup'),
    # path('login/',login,name='login'),
    # path('detail/',my_study,name='detail'),
    # path('enroll/',Enroll.as_view(),name='enroll'),
    # path('change/',change_day,name='change'),



    # main
    path('', index, name='index'),

    # user
    path('user/signup/', signup_hw, name='signup'),
    path('user/signupsns/', signup_sns, name='signup_sns'),
    path('user/login/', login_hw, name='login'),
    path('user/findid/', find_id, name='find_id'),
    path('user/findpw/', find_pw, name='find_pw'),
    path('user/resetpw/<uid64>/<token>', reset_pw, name='reset_pw'),
    path('user/checkemail/', checkemail, name='check_email'),
    path('user/activate/<uid64>/<token>', activate, name='activate'),
    path('user/logout/', logout, name='logout'),

    #kakao
    path('kakao/login',kakao_login,name='kakao_login'),
    path('kakao/callback',kakao_callback),
    path('kakao/logout',kakao_logout),

    path('user/isduplicated/',is_duplicated,name='is_duplicated'),
    path('user/resend/<email>',re_send,name='re_send'),

    # category
    path('category/inquire/', inquire, name='inquire'),
    path('category/enroll/', enroll, name='enroll'),
    path('category/change/', change, name='change'),
    path('category/faq/', faq_view, name='faq'),


    # policy

    # admin
    path('onlyadmin/<option>', only_admin, name='adminpage'),
    path('deposit_page/<option>', deposit_view, name='deposit_view'),
    path('checkdeposit/<option>/<user_id>/<way>',
         check_deposit, name='check_deposit'),
    path('checkin/<user_id>', check_in, name='check_in'),

    # error
    path('error/', testError, name='error'),

    path('uploadimg/', Img_update_view.as_view()),
    path('deleteimg/<pk>', deleteimg),

    # community
    path('noticelist/', notice_list, name='notice_list'),
    path('category/notice/detail/<num>', notice_detail, name='notice_detail'),
    path('category/notice/enroll', notice_enroll, name='notice_enroll'),
    path('category/notice/<num>', notice_view, name='notice_view'),
    #path('category/notice/delete/<pk>', notice_delete, name='notice_delete')
]
# +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
