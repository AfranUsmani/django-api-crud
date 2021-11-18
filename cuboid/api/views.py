from rest_framework import generics
from cuboid.models import Cuboid
from .serializers import CuboidSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class CuboidListAPIView(generics.ListAPIView):
    lookup_field = 'pk' # slug, id # url('<int:pk>')
    serializer_class  = CuboidSerializer
    #queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]

    filter_fields = (
        'length',
        'breadth',
        'height',
    )
    #self.request.params.min_length
    def get_queryset(self):
        qs=Cuboid.objects.all()
        if 'min_length' in self.request.query_params:
            qs=qs.filter(length__gte=self.request.query_params['min_length'])
        if 'max_length' in self.request.query_params:
            qs=qs.filter(length__lte=self.request.query_params['max_length'])
        if 'min_breadth' in self.request.query_params:
            qs=qs.filter(breadth__gte=self.request.query_params['min_breadth'])
        if 'max_breadth' in self.request.query_params:
            qs=qs.filter(breadth__lte=self.request.query_params['max_breadth'])
        if 'min_height' in self.request.query_params:
            qs=qs.filter(height__gte=self.request.query_params['min_height'])
        if 'max_height' in self.request.query_params:
            qs=qs.filter(height__lte=self.request.query_params['max_height'])
        if 'min_area' in self.request.query_params:
            qs=qs.filter(area__gte=self.request.query_params['min_area'])
        if 'max_area' in self.request.query_params:
            qs=qs.filter(area__lte=self.request.query_params['max_area'])
        if 'min_volume' in self.request.query_params:
            qs=qs.filter(volume__gte=self.request.query_params['min_volume'])
        if 'max_volume' in self.request.query_params:
            qs=qs.filter(volume__lte=self.request.query_params['max_volume'])
        return qs

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CuboidCreateAPIView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class  = CuboidSerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
       return Cuboid.objects.all()

    def perform_create(self, serializer):
        #if validate total count == L1 100 
        #return res['errors'] = 'Box count exceed'
        #   status_code = status.HTTP_400_BAD_REQUEST
        #   return JsonResponse(res, status=status_code)
        serializer.save(user=self.request.user)
    
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CuboidRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class  = CuboidSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Cuboid.objects.all()

class CuboidUserListAPIView(generics.ListAPIView):
    lookup_field = 'user'
    serializer_class  = CuboidSerializer
    permission_classes  = [IsAuthenticated]

    def get_queryset(self):
        qs=Cuboid.objects.filter(user=self.request.user)
        if 'min_length' in self.request.query_params:
            qs=qs.filter(length__gte=self.request.query_params['min_length'])
        if 'max_length' in self.request.query_params:
            qs=qs.filter(length__lte=self.request.query_params['max_length'])
        if 'min_breadth' in self.request.query_params:
            qs=qs.filter(breadth__gte=self.request.query_params['min_breadth'])
        if 'max_breadth' in self.request.query_params:
            qs=qs.filter(breadth__lte=self.request.query_params['max_breadth'])
        if 'min_height' in self.request.query_params:
            qs=qs.filter(height__gte=self.request.query_params['min_height'])
        if 'max_height' in self.request.query_params:
            qs=qs.filter(height__lte=self.request.query_params['max_height'])
        if 'min_area' in self.request.query_params:
            qs=qs.filter(area__gte=self.request.query_params['min_area'])
        if 'max_area' in self.request.query_params:
            qs=qs.filter(area__lte=self.request.query_params['max_area'])
        if 'min_volume' in self.request.query_params:
            qs=qs.filter(volume__gte=self.request.query_params['min_volume'])
        if 'max_volume' in self.request.query_params:
            qs=qs.filter(volume__lte=self.request.query_params['max_volume'])
        return qs
