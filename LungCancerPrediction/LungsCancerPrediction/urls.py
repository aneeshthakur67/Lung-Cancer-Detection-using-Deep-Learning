
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from lungs_app.views import *


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path('patient_home', User_Home,name="patient_home"),
    path('doctor_home', Doctor_Home,name="doctor_home"),
    path('admin_home', Admin_Home,name="admin_home"),
    path('about/', About,name="about"),
    path('contact/', Contact,name="contact"),
    path('gallery', Gallery,name="gallery"),
    path('login/', Login_User,name="login"),
    path('login_admin/', Login_admin,name="login_admin"),
    path('signup', Signup_User,name="signup"),
    path('logout/', Logout,name="logout"),
    path('change_password', Change_Password,name="change_password"),
    # path('prdict_heart_disease', prdict_heart_disease,name="prdict_heart_disease"),
    path('add_heartdetail', add_heartdetail,name="add_heartdetail"),
    path('view_search_pat', view_search_pat,name="view_search_pat"),

    path('view_doctor', View_Doctor,name="view_doctor"),
    path('add_doctor', add_doctor,name="add_doctor"),
    path('change_doctor/<int:pid>/', add_doctor,name="change_doctor"),
    path('view_patient', View_Patient,name="view_patient"),
    path('view_feedback', View_Feedback,name="view_feedback"),
    path('edit_profile', Edit_My_deatail,name="edit_profile"),
    path('profile_doctor', View_My_Detail,name="profile_doctor"),
    path('sent_feedback', sent_feedback,name="sent_feedback"),

    path('delete_searched/<int:pid>', delete_searched, name="delete_searched"),
    path('delete_doctor<int:pid>', delete_doctor, name="delete_doctor"),
    path('assign_status<int:pid>', assign_status, name="assign_status"),
    path('delete_patient<int:pid>', delete_patient, name="delete_patient"),
    path('delete_feedback<int:pid>', delete_feedback, name="delete_feedback"),
    path('predict_desease/<str:pred>/<str:accuracy>/', predict_desease, name="predict_desease"),

    path('add_genralhealth', add_genralhealth, name="add_genralhealth"),

    path('search_blood', search_blood, name="search_blood"),
    path('donate_blood', donate_blood, name="donate_blood"),

    path('request_blood', request_blood, name="request_blood"),
    path('donator_blood', donator_blood, name="donator_blood"),

    path('change_status/<int:pid>/', change_status, name="change_status"),

    path('add_lungs_pred', add_lungs_pred, name="add_lungs_pred"),
    path('detail_searched/<int:pid>', detail_searched, name="detail_searched"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
