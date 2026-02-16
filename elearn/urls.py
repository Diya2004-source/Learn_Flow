from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # for apps
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('enrollments/', include('enrollments.urls')),
    path('payments/', include('payments.urls')),
    path('progress/', include('progress.urls')),
    path('quiz/', include('quiz.urls')),
    path('certificates/', include('certificate.urls')),
    path('ai/', include('ai_assistant.urls')),
]

# for images (only in development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
