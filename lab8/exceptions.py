class MemeGeneratorError(Exception):
    """Базовое исключение приложения"""
    pass


class ImageNotLoadedError(MemeGeneratorError):
    """Ошибка отсутствия изображения"""
    pass


class SaveImageError(MemeGeneratorError):
    """Ошибка сохранения изображения"""
    pass