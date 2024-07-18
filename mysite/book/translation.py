from .models import Hotel
from modeltranslation.translator import TranslationOptions,register

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('name_hotel', 'description', 'address', 'city', 'country')