from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FlashcardSetViewSet, FlashcardViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sets', FlashcardSetViewSet)
router.register(r'cards', FlashcardViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls
