from django.urls import path
from main.views import show_item, create_item, register_account,login_user, logout_user, show_xml, show_json, show_xml_by_id, show_json_by_id, increase_item, decrease_item, delete

app_name = 'main'

urlpatterns = [
    path('ingredients-collection', show_item, name='ingredients-collection'),
    path('create_item',create_item,name= 'create_item'),
    path('register/', register_account, name ='register_acc'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('item/<int:id>/increase_item/', increase_item, name='increase_item'),
    path('item/<int:id>/decrease_item/', decrease_item, name='decrease_item'),
    path('item/<int:id>/delete/', delete, name='delete'),
]