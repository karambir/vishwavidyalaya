# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Student.name'
        db.delete_column('profiles_student', 'name')

        # Adding field 'Student.first_name'
        db.add_column('profiles_student', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='Mayank', max_length=200),
                      keep_default=False)

        # Adding field 'Student.last_name'
        db.add_column('profiles_student', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='Jain', max_length=200),
                      keep_default=False)

        # Adding field 'Student.birth_date'
        db.add_column('profiles_student', 'birth_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.alternate_phone'
        db.add_column('profiles_student', 'alternate_phone',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.address'
        db.add_column('profiles_student', 'address',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='student_address', null=True, to=orm['profiles.Address']),
                      keep_default=False)


        # Changing field 'Student.phone'
        db.alter_column('profiles_student', 'phone', self.gf('django.db.models.fields.BigIntegerField')(null=True))

    def backwards(self, orm):
        # Adding field 'Student.name'
        db.add_column('profiles_student', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Jain', max_length=200),
                      keep_default=False)

        # Deleting field 'Student.first_name'
        db.delete_column('profiles_student', 'first_name')

        # Deleting field 'Student.last_name'
        db.delete_column('profiles_student', 'last_name')

        # Deleting field 'Student.birth_date'
        db.delete_column('profiles_student', 'birth_date')

        # Deleting field 'Student.alternate_phone'
        db.delete_column('profiles_student', 'alternate_phone')

        # Deleting field 'Student.address'
        db.delete_column('profiles_student', 'address_id')


        # Changing field 'Student.phone'
        db.alter_column('profiles_student', 'phone', self.gf('django.db.models.fields.IntegerField')(null=True))

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
            'address': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'student_address'", 'null': 'True', 'to': "orm['profiles.Address']"}),
            'alternate_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Course']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'enrolment_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'exam_roll': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'form_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Section']"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['academics.Subject']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['profiles']