# @register(Direction)
# class DirectionTranslationOptions(TranslationOptions):
#     fields = (
#         'name',
#     )



from modeltranslation.translator import translator, TranslationOptions, register
from .models import *



@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )
@register(Index)
class IndexTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )
@register(ContactUs)
class ContactUsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )
@register(Park)
class ParkTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )
@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )
