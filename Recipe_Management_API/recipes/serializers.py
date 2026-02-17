from rest_framework import serializers
from .models import Category, Ingredient, Recipe, RecipeIngredient


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.StringRelatedField()

    class Meta:
        model = RecipeIngredient
        fields = ["ingredient"]


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "description",
            "instructions",
            "prep_time",
            "cook_time",
            "servings",
            "created_at",
            "author",
            "category",
            "ingredients",
        ]
