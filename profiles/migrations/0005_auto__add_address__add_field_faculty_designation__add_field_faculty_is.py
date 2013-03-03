# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table('profiles_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('pincode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('profiles', ['Address'])

        # Adding field 'Faculty.designation'
        db.add_column('profiles_faculty', 'designation',
                      self.gf('django.db.models.fields.CharField')(default='B.Tech', max_length=50),
                      keep_default=False)

        # Adding field 'Faculty.is_admin'
        db.add_column('profiles_faculty', 'is_admin',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Faculty.qualification'
        db.add_column('profiles_faculty', 'qualification',
                      self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Faculty.experience'
        db.add_column('profiles_faculty', 'experience',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Faculty.school'
        db.add_column('profiles_faculty', 'school',
                      self.gf('django.db.models.fields.CharField')(default='ASET', max_length=300),
                      keep_default=False)

        # Adding field 'Faculty.marital_status'
        db.add_column('profiles_faculty', 'marital_status',
                      self.gf('django.db.models.fields.CharField')(default='Single', max_length=30),
                      keep_default=False)

        # Adding field 'Faculty.alternate_phone'
        db.add_column('profiles_faculty', 'alternate_phone',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Faculty.permanent_address'
        db.add_column('profiles_faculty', 'permanent_address',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='permanent_address', null=True, to=orm['profiles.Address']),
                      keep_default=False)

        # Adding field 'Faculty.correspondence_address'
        db.add_column('profiles_faculty', 'correspondence_address',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='correspondence_address', null=True, to=orm['profiles.Address']),
                      keep_default=False)

        # Adding field 'Faculty.description'
        db.add_column('profiles_faculty', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table('profiles_address')

        # Deleting field 'Faculty.designation'
        db.delete_column('profiles_faculty', 'designation')

        # Deleting field 'Faculty.is_admin'
        db.delete_column('profiles_faculty', 'is_admin')

        # Deleting field 'Faculty.qualification'
        db.delete_column('profiles_faculty', 'qualification')

        # Deleting field 'Faculty.experience'
        db.delete_column('profiles_faculty', 'experience')

        # Deleting field 'Faculty.school'
        db.delete_column('profiles_faculty', 'school')

        # Deleting field 'Faculty.marital_status'
        db.delete_column('profiles_faculty', 'marital_status')

        # Deleting field 'Faculty.alternate_phone'
        db.delete_column('profiles_faculty', 'alternate_phone')

        # Deleting field 'Faculty.permanent_address'
        db.delete_column('profiles_faculty', 'permanent_address_id')

        # Deleting field 'Faculty.correspondence_address'
        db.delete_column('profiles_faculty', 'correspondence_address_id')

        # Deleting field 'Faculty.description'
        db.delete_column('profiles_faculty', 'description')


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
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pincode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'})
        },
        'profiles.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'alternate_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'correspondence_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'correspondence_address'", 'null': 'True', 'to': "orm['profiles.Address']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'empID': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'experience': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'permanent_address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'permanent_address'", 'null': 'True', 'to': "orm['profiles.Address']"}),
            'phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'profiles.student': {
            'Meta': {'object_name': 'Student'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Course']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'enrolment_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'exam_roll': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'form_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Section']"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['academics.Subject']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiles']