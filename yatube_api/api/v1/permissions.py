from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Класс permissions для доступа к постам и комментариям.
    Доступ на чтение предоставляется всем пользователям - аутентифицированным
    и неаутентифицированным.
    Доступ на изменение объекта - только к своим постам.
    Создание объекта - только для аутентифицированных.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
