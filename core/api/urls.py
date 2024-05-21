from django.urls import path
from ninja import NinjaAPI

from core.api.schemas import PingResponceSchema
from core.api.v1.urls import router as v1_router

api = NinjaAPI()


@api.get("/ping", response=PingResponceSchema)
def ping(request) -> PingResponceSchema:
    return PingResponceSchema(result=True)


api.add_router("v1/", v1_router)


urlpatterns = [
    path("", api.urls),
]
