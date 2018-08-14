from django.contrib import admin

# Register your models here.

from web.models import User, Node, UserPreference, Tag, Relation, Similarity

admin.site.register(User)
admin.site.register(Node)
admin.site.register(Tag)
admin.site.register(Relation)
admin.site.register(UserPreference)
admin.site.register(Similarity)

