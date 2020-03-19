from django.urls import path
from.import views

urlpatterns = [
    path("",views.home,name="home"),
    path("add_camera/",views.add_camera,name="add_camera"),
    path("view_camera/",views.view_camera,name="view_camera"),
    path('edit/<int:id>', views.edit),
    #Update Contact
    #localhost:8000/update/<ID>
    path('update/<int:id>', views.update),
    #Delete Contact
    ##localhost:8000/delete/<ID>
    path('delete/<int:id>', views.delete),
    path("Linear/",views.linear,name="linear"),
    path("logistic/",views.logistic,name="logistic"),


    path("company_login",views.company_login,name="company_login"),
    path("company_register",views.company_register,name="company_register"),
    path("batch",views.batch,name='batch'),
    path("person_entry",views.person_entry,name='person_entry')



]
