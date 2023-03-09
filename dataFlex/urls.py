from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="dataFlex API",
        default_version='v0.0.1',
        description="Projeto desenvolvido para fins comparativos entre o desempenho dos bancos de dados, Postgresql e MongoDB",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="gerson.silva@arapiraca.ufal.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path(''      , schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]
