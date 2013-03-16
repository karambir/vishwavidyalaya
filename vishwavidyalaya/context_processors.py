from profiles.models import Faculty, Director

def navigation(request):
    logged_user = request.user
    is_hod = False
    is_director = False
    is_coordinator = False
    if logged_user.is_authenticated():
        try:
            u = Director.objects.get(user=logged_user)
            is_director = True
        except:
            u = Faculty.objects.get(user=logged_user)
            is_hod = u.is_hod()
            is_coordinator = u.is_coordinator()
    return {'is_hod': is_hod, 'is_director': is_director}
