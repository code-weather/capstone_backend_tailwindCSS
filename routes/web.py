"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Get("/", "QuoteController@index").name("index"),
        Get("/@id", "QuoteController@show").name("show"),
        Post("/", "QuoteController@create").name("create"),
        Put("/@id", "QuoteController@update").name("update"),
        Delete("/@id", "QuoteController@destroy").name("destroy")
    ], prefix="/quotes", name="quotes")
]