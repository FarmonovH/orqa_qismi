from rest_framework import serializersfrom .models import Social_links, Portfolio, Visitors, Portfolio_project, Info, Xabarlarclass SocialSerializers(serializers.ModelSerializer):    class Meta:        model = Social_links        fields = '__all__'class PortfolioSerializers(serializers.ModelSerializer):    class Meta:        model = Portfolio        fields = '__all__'class VisitorSerializers(serializers.ModelSerializer):    passclass Portfolio_projects(serializers.ModelSerializer):    class Meta:        model = Portfolio_project        fields = '__all__'class InfoSerializers(serializers.ModelSerializer):    class Meta:        model = Info        fields = '__all__'class XabarlarSerializers(serializers.ModelSerializer):    class Meta:        model = Xabarlar        fields = '__all__'