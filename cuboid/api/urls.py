from django.conf.urls import url

#from .views import CuboidListAPIView, CuboidRudView, CuboidCreateAPIView

#app_name = 'cuboid-api'
app_name = ['cuboid-api','cuboid-create','cuboid-rud','cuboid-listcreate','cuboid-retrieve']

urlpatterns = [
    #url('', CuboidListAPIView.as_view(), name='cuboid-listcreate'),
    #url('Add/<int:pk>', CuboidCreateAPIView.as_view(), name='cuboid-create'),
    #url('(?P<pk>\d+)/', CuboidRudView.as_view(), name='cuboid-rud'),
    #url('<int:pk>', CuboidRudView.as_view(), name='cuboid-rud')
]   