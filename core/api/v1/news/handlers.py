from django.http import HttpRequest
from ninja import Router

from core.api.v1.news.schemas import NewsListSchema

router = Router(tags=["News"])


@router.get("", response=NewsListSchema)
def get_product_list_handler(request: HttpRequest) -> NewsListSchema:
    return []
