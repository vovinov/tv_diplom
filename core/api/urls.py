from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/ping")
def ping(request):
    return {"result": True}


urlpatterns = [
    path("", api.urls),
]
