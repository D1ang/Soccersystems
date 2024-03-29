from django.shortcuts import redirect


def allowed_users(allowed_roles=None):
    '''
    Looks for the user group & checks
    if an employee has admin rights to view the admin dashboard.
    If not, the employee will be redirected.
    '''

    # Python Mutable Defaults fix
    if allowed_roles is None:
        allowed_roles = []
    
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                if request.user.is_superuser:
                    return redirect('accounts:admin')
                else:
                    return redirect('accounts:supervisor')
                    
        return wrapper_func
    return decorator
