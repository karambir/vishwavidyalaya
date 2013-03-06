# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'timetable'
        db.create_table('timetable_timetable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_type', self.gf('django.db.models.fields.CharField')(default='Free', max_length=20)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['academics.Section'])),
            ('weekday', self.gf('django.db.models.fields.CharField')(default='Monday', max_length=10)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['academics.Subject'])),
        ))
        db.send_create_signal('timetable', ['timetable'])


    def backwards(self, orm):
        # Deleting model 'timetable'
        db.delete_table('timetable_timetable')


    models = {
        'academics.course': {
            'Meta': {'object_name': 'Course'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'academics.section': {
            'Meta': {'object_name': 'Section'},
            'batch': ('django.db.models.fields.IntegerField', [], {}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['academics.Course']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'academics.subject': {
            'Meta': {'object_name': 'Subject'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'timetable.timetable': {
            'Meta': {'object_name': 'timetable'},
            'class_type': ('django.db.models.fields.CharField', [], {'default': "'Free'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Section']"}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Subject']"}),
            'weekday': ('django.db.models.fields.CharField', [], {'default': "'Monday'", 'max_length': '10'})
        }
    }

    complete_apps = ['timetable']