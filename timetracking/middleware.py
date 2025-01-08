from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.user.is_authenticated and request.user.is_staff and not request.user.is_superuser:
            # return redirect('moderator_home')
            raise PermissionDenied
        response = self.get_response(request)
        return response