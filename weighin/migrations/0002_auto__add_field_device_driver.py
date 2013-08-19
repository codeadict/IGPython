# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Device.driver'
        db.add_column(u'weighin_device', 'driver',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Device.driver'
        db.delete_column(u'weighin_device', 'driver')


    models = {
        u'weighin.device': {
            'Meta': {'ordering': "('-default',)", 'object_name': 'Device'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'driver': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'port': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['weighin']