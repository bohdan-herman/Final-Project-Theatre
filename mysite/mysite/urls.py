from django.contrib import admin
from django.urls import path, include
from myapp.views import MainPageView, ContactsPageView, ProgramPageView, AboutUsPageView, PartnersPageView, TicketsPageView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', include('myapp.play_url')),
    path('carousel/', include('myapp.carousel_url')),
    path('', MainPageView.as_view(), name = "main_page"),
    path('contacts/', ContactsPageView.as_view(), name = "contacts_page"),
    path('program/', ProgramPageView.as_view(), name = "program_page"),
    path('about-us/', AboutUsPageView.as_view(), name = "about_us_page"),
    path('partners/', PartnersPageView.as_view(), name = "partners_page"),
    path('tickets/', TicketsPageView.as_view(), name = "tickets_page"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)