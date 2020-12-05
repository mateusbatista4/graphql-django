import graphene
from graphene_django import DjangoObjectType
from movie.models import Movie, Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "movies")

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = ("id", "name", "director","release_year", "category")
    
class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_movies(root, info):
        # We can easily optimize query count in the resolve method
        return Movie.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)