def validate_md(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.md']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
