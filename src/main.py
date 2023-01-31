from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from config import Config
from routers.launcher import router as router_launch
import uvicorn


def welcome():
    """Simple welcome message"""
    print(r"""
╔════╦═══╦═══╦╗──╔╦══╦╗─╔╦══╦════╦══╦══╦╗─╔╗
╚═╗╔═╣╔══╣╔═╗║║──║╠╗╔╣╚═╝║╔╗╠═╗╔═╩╗╔╣╔╗║╚═╝║
──║║─║╚══╣╚═╝║╚╗╔╝║║║║╔╗─║╚╝║─║║──║║║║║║╔╗─║
──║║─║╔══╣╔╗╔╣╔╗╔╗║║║║║╚╗║╔╗║─║║──║║║║║║║╚╗║
──║║─║╚══╣║║║║║╚╝║╠╝╚╣║─║║║║║─║║─╔╝╚╣╚╝║║─║║
──╚╝─╚═══╩╝╚╝╚╝──╚╩══╩╝─╚╩╝╚╝─╚╝─╚══╩══╩╝─╚╝
    """)
    print("\n")


app = FastAPI()
app.include_router(router_launch)

openapi_schema = get_openapi(
    title="Termination Tickets API",
    version="1.0",
    routes=app.routes,
)
openapi_schema["info"] = {
    "title": "Termination Tickets API",
    "version": "1.0",
    "description": "Automatic assignee to unassigned by user id, "
                   "create termination tickets and link them."
                   "\"Launch termination\" starts the process of termination user.",
}
app.openapi_schema = openapi_schema
if __name__ == "__main__":
    welcome()
    config = Config()
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)