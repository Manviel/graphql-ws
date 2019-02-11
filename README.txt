### Django Channels 2

Set up with Django Channels just takes three steps:

1. Install the apps
2. Set up your schema
3. Configure the channels router application


First `pip install channels` and it to your `INSTALLED_APPS`. If you want
graphiQL, install the `graphql_ws.django` app before `graphene_django` to serve
a graphiQL template that will work with websockets:

```python
INSTALLED_APPS = [
    "channels",
    "graphql_ws.django",
    "graphene_django",
    # ...
]
```


Next, set up your graphql schema:

```python
import graphene
from rx import Observable


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info, **kwargs):
        return "world"


class Subscription(graphene.ObjectType):

    count_seconds = graphene.Int(up_to=graphene.Int())

    def resolve_count_seconds(root, info, up_to=5):
        return (
            Observable.interval(1000)
            .map(lambda i: "{0}".format(i))
            .take_while(lambda i: int(i) <= up_to)
        )


schema = graphene.Schema(query=Query, subscription=Subscription)
```

...and point to your schema in Django settings
```python
GRAPHENE = {
    'SCHEMA': 'yourproject.schema'
}
```


Finally, you can set up channels routing yourself (maybe using
`graphql_ws.django.routing.websocket_urlpatterns` in your `URLRouter`), or you
can just use one of the preset channels applications:

```python
ASGI_APPLICATION = 'graphql_ws.django.routing.application'
# or
ASGI_APPLICATION = 'graphql_ws.django.routing.auth_application'
```

Run `./manage.py runserver` and go to `http://localhost:8000/graphql` to test!
