from django.urls import path

from firstapp.views import index, first, third

app_name="firstapp"
# 들어오고자 하는 경로: "127.0.0.1:8000/account/hello_world" <=> accountapp:firstpage_name

urlpatterns = [
    path("", index, name=""),
    path("index.html", index, name=""),
    path("1.html", first, name=""),
    path("3.html", third, name="")
]

