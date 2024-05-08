from django.utils.translation import get_language


def get_field_by_language(self, field_name):
    field = getattr(self, f'{field_name}_{get_language()}')
    if not field:
        return getattr(self, f'{field_name}_uz')
    return field
