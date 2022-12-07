from django.shortcuts import render
from .models import Social_links, Portfolio, Visitors, Portfolio_project, Info, Xabarlar
from .serializers import SocialSerializers, PortfolioSerializers,VisitorSerializers, Portfolio_projects, InfoSerializers, XabarlarSerializers
from rest_framework.viewsets import ModelViewSet
from .pagination import MyProjectPagination
# Create your views here.
class SocialViewset(ModelViewSet):
    queryset = Social_links.objects.all().order_by('-id')[:1]
    serializer_class = SocialSerializers



class PortfolioViewset(ModelViewSet):
    queryset = Portfolio.objects.all().order_by('id')[:1]
    serializer_class = PortfolioSerializers


class ProjectViewset(ModelViewSet):
    queryset = Portfolio_project.objects.all()
    serializer_class = Portfolio_projects
    pagination_class = MyProjectPagination



class InfoViewset(ModelViewSet):
    queryset = Info.objects.all().order_by('id')[:1]
    serializer_class = InfoSerializers



class XabarlarViewset(ModelViewSet):
    queryset = Xabarlar.objects.all()
    serializer_class = XabarlarSerializers


