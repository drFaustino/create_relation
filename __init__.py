# -*- coding: utf-8 -*-

def classFactory(iface):
    """Load CreateRelation plugin."""

    from .create_relation import CreateRelation
    return CreateRelation(iface)