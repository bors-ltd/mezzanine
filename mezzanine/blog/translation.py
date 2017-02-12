from modeltranslation.translator import translator
from mezzanine.core.translation import (TranslatedSlugged,
                                        TranslatedDisplayable,
                                        TranslatedRichText)
from mezzanine.blog.models import BlogCategory, BlogPost


class TranslatedBlogPost(TranslatedDisplayable, TranslatedRichText):
    fields = ()


class TranslatedBlogCategory(TranslatedSlugged):
    fields = ()


# XXX What about swapped models?
translator.register(BlogCategory, TranslatedBlogCategory)
translator.register(BlogPost, TranslatedBlogPost)
