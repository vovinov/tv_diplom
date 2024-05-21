from ninja import Router
from core.api.v1.news.handlers import router as news_router

router = Router(tags=["v1"])
router.add_router("news/", news_router)
