from werkzeug.security import check_password_hash, generate_password_hash


_USERS = [
    {
        "id": 1,
        "username": "alumno",
        "password_hash": generate_password_hash("Taller2026!"),
        "is_active": True,
    },
    {
        "id": 2,
        "username": "instructor",
        "password_hash": generate_password_hash("Instructor2026!"),
        "is_active": True,
    },
]


def find_user_by_id(user_id):
    # TODO SESIÓN 2: cuando DATA_MODE sea database, consultar User por su id.
    return next((user for user in _USERS if user["id"] == user_id), None)


def authenticate(username, password):
    # TODO SESIÓN 2: sustituir la búsqueda en _USERS por una consulta de User.
    # Mantener la verificación del hash y la condición is_active.
    normalized_username = username.strip().lower()
    user = next(
        (
            item
            for item in _USERS
            if item["username"] == normalized_username and item["is_active"]
        ),
        None,
    )

    if user and check_password_hash(user["password_hash"], password):
        return user
    return None
