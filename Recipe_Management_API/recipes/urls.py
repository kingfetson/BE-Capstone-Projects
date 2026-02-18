from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, IngredientViewSet, RecipeViewSet

# Create a single router
router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"ingredients", IngredientViewSet, basename="ingredients")
router.register(r"recipes", RecipeViewSet, basename="recipes")

# Expose the router URLs
urlpatterns = router.urls
