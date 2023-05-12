import os.path


def get_image_path_name(instance, filename: str) -> str:
    """Содает путь для хранения картинки"""
    suffix = instance.dish.images.all().count() + 1
    ext = os.path.splitext(filename)[1]
    slug = instance.dish.slug
    return f'dish_image/{slug}/{slug}_{suffix}{ext}'
