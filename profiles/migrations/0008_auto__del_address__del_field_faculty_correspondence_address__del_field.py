# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Faculty', fields ['empID']
        db.delete_unique('profiles_faculty', ['empID'])

        # Deleting model 'Address'
        db.delete_table('profiles_address')

        # Deleting field 'Faculty.correspondence_address'
        db.delete_column('profiles_faculty', 'correspondence_address_id')

        # Deleting field 'Faculty.permanent_address'
        db.delete_column('profiles_faculty', 'permanent_address_id')

        # Adding field 'Faculty.address_street'
        db.add_column('profiles_faculty', 'address_street',
                      self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Faculty.address_city'
        db.add_column('profiles_faculty', 'address_city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Faculty.address_state'
        db.add_column('profiles_faculty', 'address_state',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Faculty.address_pincode'
        db.add_column('profiles_faculty', 'address_pincode',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Faculty.is_mentor'
        db.add_column('profiles_faculty', 'is_mentor',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Faculty.empID'
        db.alter_column('profiles_faculty', 'empID', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Deleting field 'Student.address'
        db.delete_column('profiles_student', 'address_id')

        # Adding field 'Student.address_street'
        db.add_column('profiles_student', 'address_street',
                      self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.address_city'
        db.add_column('profiles_student', 'address_city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.address_state'
        db.add_column('profiles_student', 'address_state',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.address_pincode'
        db.add_column('profiles_student', 'address_pincode',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Address'
        db.create_table('profiles_address', (
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('pincode', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('profiles', ['Address'])

        # Adding field 'Faculty.correspondence_address'
        db.add_column('profiles_faculty', 'correspondence_address',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='correspondence_address', null=True, to=orm['profiles.Address'], blank=True),
                      keep_default=False)

        # Adding field 'Faculty.permanent_address'
        db.add_column('profiles_faculty', 'permanent_address',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='permanent_address', null=True, to=orm['profiles.Address'], blank=True),
                      keep_default=False)

        # Deleting field 'Faculty.address_street'
        db.delete_column('profiles_faculty', 'address_street')

        # Deleting field 'Faculty.address_city'
        db.delete_column('profiles_faculty', 'address_city')

        # Deleting field 'Faculty.address_state'
        db.delete_column('profiles_faculty', 'address_state')

        # Deleting field 'Faculty.address_pincode'
        db.delete_column('profiles_faculty', 'address_pincode')

        # Deleting field 'Faculty.is_mentor'
        db.delete_column('profiles_faculty', 'is_mentor')


        # Changing field 'Faculty.empID'
        db.alter_column('profiles_faculty', 'empID', self.gf('django.db.models.fields.IntegerField')(default='1414', unique=True))
        # Adding unique constraint on 'Faculty', fields ['empID']
        db.create_unique('profiles_faculty', ['empID'])

        # Adding field 'Student.address'
        db.add_column('profiles_student', 'address',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='student_address', null=True, to=orm['profiles.Address'], blank=True),
                      keep_default=False)

        # Deleting field 'Student.address_street'
        db.delete_column('profiles_student', 'address_street')

        # Deleting field 'Student.address_city'
        db.delete_column('profiles_student', 'address_city')

        # Deleting field 'Student.address_state'
        db.delete_column('profiles_student', 'address_state')

        # Deleting field 'Student.address_pincode'
        db.delete_column('profiles_student', 'address_pincode')


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
        'profiles.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_pincode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'alternate_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'empID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'experience': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_mentor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'profiles.student': {
            'Meta': {'object_name': 'Student'},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_pincode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'alternate_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Course']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'enrolment_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'exam_roll': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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