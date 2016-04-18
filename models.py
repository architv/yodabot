from google.appengine.ext import ndb

class Games(ndb.Model):
    """Models Contests"""
    data = ndb.TextProperty(default="{}")
    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)