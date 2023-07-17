from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://amili.ddns.net",
    "http://localhost:5173",
]


def cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
