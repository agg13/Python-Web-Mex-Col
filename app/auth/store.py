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
    return next((user for user in _USERS if user["id"] == user_id), None)


def authenticate(username, password):
    """Devuelve el usuario cuando las credenciales son válidas."""

    # TODO SESIÓN 1:
    # 1. Normalizar username.
    # 2. Buscar un usuario activo.
    # 3. Comparar password con password_hash mediante check_password_hash.
    # 4. Devolver el usuario válido o None.
    _ = username, password, check_password_hash
    return None
