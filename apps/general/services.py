from django.utils.translation import get_language


def get_field_by_language(self, field_name):
    return getattr(self, f'{field_name}_{get_language()}')
