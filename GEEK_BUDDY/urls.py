"""GEEK_BUDDY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from GEEKBUUDY import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('userhome',views.userhome,name='userhome'),
    path('Companyhome',views.companyhome,name='Companyhome'),
    path('Adminhome',views.adminhome,name='adminhome'),
    path('CompanySignup',   views.CompanySignup, name='CompanySignup'),
    path('addProduct',  views.Addproduct,name="AddProduct"),
    path('compare<int:id>', views.compare,name="compare"),
    path('compareview<int:id>', views.compareview,name="compareview"),
    path('mycomment<int:id>', views.mycomment,name="mycomment"),
    path('prodectdetails<int:id>', views.prodectdetails, name='prodectdetails'),
    path('deleteproduct<int:id>', views.deleteproduct, name='deleteproduct'),
    path('ALLProduct',  views.ALLProduct,name="ALLProduct"),
    path('AdminALLProduct',  views.AdminALLProduct,name="AdminALLProduct"),
    path('Adminproductdetails<int:id>',  views.Adminproductdetails,name="Adminproductdetails"),
    path('AdminCommentDelete<int:id>', views.AdminCommentDelete, name='AdminCommentDelete'),
    path('AdminALLUsers',  views.AdminALLUsers,name="AdminALLUsers"),
    path('Companyproductdetails<int:id>',  views.Companyproductdetails,name="Companyproductdetails"),
    path('CompanyALLProduct<int:id>',  views.CompanyALLProduct,name="CompanyALLProduct"),
    path('Adminviewallusers',  views.Adminviewallusers,name="Adminviewallusers"),
    path('Admindeleteusers<int:id>', views.Admindeleteusers, name='Admindeleteusers'),
    path('Adminviewallcompany',  views.Adminviewallcompany,name="Adminviewallcompany"),
    path('AdminApproveCompany<int:id>', views.AdminApproveCompany, name='AdminApproveCompany'),
    path('AdminRejectCompany<int:id>', views.AdminRejectCompany, name='AdminRejectCompany'),
    path('AdminDeleteCompany<int:id>', views.AdminDeleteCompany, name='AdminDeleteCompany'),
    path('AdminApprovedCompanyview', views.AdminApprovedCompanyview, name="AdminApprovedCompanyview"),
    path('AdminRejectedCompanyview', views.AdminRejectedCompanyview, name="AdminRejectedCompanyview"),







]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
