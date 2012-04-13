# -*- coding: utf-8 -*-
from django.forms import ModelForm

from tablon.models import Post

class PostHijosForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('hijo', 'published_by')
        
    def save(self, hijos, publisher, **kwargs):
        instance = super(PostHijosForm, self).save(commit=False)
        
        if len(hijos) > 0:
            for hijo in hijos:
                instance.hijo = hijo
                instance.published_by = publisher
                done = instance.save()
                instance.id = none
        else:
            instance.published_by = publisher
            
            #siguiente l’nea es una CHAPUZA
            instance.hijo_id = 0
            done = instance.save()
        
        return done

