from django.urls import path

from . import views

app_name = "proyecto"
urlpatterns = [
    path("", views.ProyectoListView.as_view(), name="index"),
    path("<int:pk>/", views.ProyectoDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.ProyectoUpdateView.as_view(), name="update"),
    path("create/", views.ProyectoCreateView.as_view(), name="create"),
    path("<int:pk>/delete/", views.ProyectoDeleteView.as_view(), name="delete"),
    #path("facturas", views.FacturaListView.as_view(), name="factura-index"),
    #path("facturas/<int:pk>/", views.FacturaDetailView.as_view(), name="factura-detail"),
    #path("facturas/<int:pk>/update/", views.FacturaUpdateView.as_view(), name="factura-update"),
    #path("facturas/create/", views.FacturaCreateView.as_view(), name="factura-create"),
    #path("facturas/<int:pk>/delete/", views.FacturaDeleteView.as_view(), name="factura-delete"),
]