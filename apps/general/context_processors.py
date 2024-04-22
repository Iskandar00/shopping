from apps.general.models import General


def general(request):
    return {'generals': General.objects.all()}
