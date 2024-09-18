from ninja import NinjaAPI


# from posts.api import router as post_router
api = NinjaAPI()


# or by Python path



api.add_router("/users/", "users.api.router")
api.add_router("/flights/", "flights.api.router")
api.add_router("/tickets/", "tickets.api.router")
api.add_router("/checkins/", "checkins.api.router")
api.add_router("/passenger/", "passenger.api.router")
api.add_router("/adjustments/", "adjustments.api.router")








