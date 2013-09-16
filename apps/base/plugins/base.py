from django.utils.translation import ugettext as _

"""Base classes for different plugin objects.

* BasePlugin: Create a ow_plugin.py with a class that inherits from BasePlugin.
* PluginSettingsFormMixin: ..and this one for a form in the settings tab.

Please have a look in wiki.models.pluginbase to see where to inherit your
plugin's models.
"""
from django import forms

class BasePlugin(object):
    """Plugins should inherit from this"""
    slug = None
    
    # Optional
    settings_form = None# A form class to add to the settings tab
    
    urlpatterns = {
        'root': [], # General urlpatterns that will reside in /plugins/plugin-slug/...
    }
    menu_tab = None #(_(u'Attachments'), url, "icon")
    
    plugin_view = None # A view for Plugin
    
    class RenderMedia:
        js = []
        css = {}
 
        
class PluginSettingsFormMixin(object):
    settings_form_headline = _(u'Settings for plugin')
    settings_order = 1
    
    def get_usermessage(self):
        pass