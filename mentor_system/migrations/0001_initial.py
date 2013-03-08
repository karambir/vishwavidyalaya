# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mentor'
        db.create_table('mentor_system_mentor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('faculty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Faculty'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Section'])),
            ('group', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Session'])),
        ))
        db.send_create_signal('mentor_system', ['Mentor'])

        # Adding model 'Mentee'
        db.create_table('mentor_system_mentee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['profiles.Student'], unique=True)),
            ('present_address', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('present_address_phone', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('present_address_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('permanent_address', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('permanent_address_phone', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('permanent_address_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('local_guardian_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('local_guardian_address', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('local_guardian_phone', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('local_guardian_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('school_board', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('school_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('school_division', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('school_remarks', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('inter_board', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('inter_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('inter_division', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('inter_remarks', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('degree_board', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('degree_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('degree_division', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('degree_remarks', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('others_board', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('others_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('others_division', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('others_remarks', self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True)),
            ('family1_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('family1_relationship', self.gf('django.db.models.fields.CharField')(default='Father', max_length=20, null=True, blank=True)),
            ('family1_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('family1_qualification', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('family2_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('family2_relationship', self.gf('django.db.models.fields.CharField')(default='Mother', max_length=20, null=True, blank=True)),
            ('family2_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('family2_qualification', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('family3_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('family3_relationship', self.gf('django.db.models.fields.CharField')(default='Brother', max_length=20, null=True, blank=True)),
            ('family3_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('family3_qualification', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('family4_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('family4_relationship', self.gf('django.db.models.fields.CharField')(default='Brother', max_length=20, null=True, blank=True)),
            ('family4_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('family4_qualification', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('family5_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('family5_relationship', self.gf('django.db.models.fields.CharField')(default='Sister', max_length=20, null=True, blank=True)),
            ('family5_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('family5_qualification', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('special_achievements', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('interests', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('additional_information', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('emergency1_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('emergency1_location', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('emergency1_phone', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('emergency2_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('emergency2_location', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('emergency2_phone', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('mentor_system', ['Mentee'])

        # Adding model 'Meeting'
        db.create_table('mentor_system_meeting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentor_system.Mentor'])),
            ('mentee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentor_system.Mentee'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('remarks', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Session'])),
        ))
        db.send_create_signal('mentor_system', ['Meeting'])


    def backwards(self, orm):
        # Deleting model 'Mentor'
        db.delete_table('mentor_system_mentor')

        # Deleting model 'Mentee'
        db.delete_table('mentor_system_mentee')

        # Deleting model 'Meeting'
        db.delete_table('mentor_system_meeting')


    models = {
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
        'mentor_system.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentor_system.Mentee']"}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentor_system.Mentor']"}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Session']"})
        },
        'mentor_system.mentee': {
            'Meta': {'object_name': 'Mentee'},
            'additional_information': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'degree_board': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'degree_division': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'degree_remarks': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'degree_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'emergency1_location': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'emergency1_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'emergency1_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'emergency2_location': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'emergency2_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'emergency2_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family1_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family1_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family1_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family1_relationship': ('django.db.models.fields.CharField', [], {'default': "'Father'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'family2_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family2_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family2_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family2_relationship': ('django.db.models.fields.CharField', [], {'default': "'Mother'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'family3_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family3_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family3_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family3_relationship': ('django.db.models.fields.CharField', [], {'default': "'Brother'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'family4_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family4_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family4_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family4_relationship': ('django.db.models.fields.CharField', [], {'default': "'Brother'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'family5_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family5_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family5_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family5_relationship': ('django.db.models.fields.CharField', [], {'default': "'Sister'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inter_board': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'inter_division': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'inter_remarks': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'inter_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'interests': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'local_guardian_address': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'local_guardian_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'local_guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'local_guardian_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'others_board': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'others_division': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'others_remarks': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'others_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'permanent_address': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'permanent_address_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'permanent_address_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'present_address': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'present_address_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'present_address_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'school_board': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'school_division': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'school_remarks': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'school_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'special_achievements': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['profiles.Student']", 'unique': 'True'})
        },
        'mentor_system.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'faculty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Faculty']"}),
            'group': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Section']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Session']"})
        },
        'profiles.faculty': {
            'Meta': {'object_name': 'Faculty'},
            'address_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address_pincode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'address_state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'alternate_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'empID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'experience': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'profiles.student': {
            'Meta': {'object_name': 'Student'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Course']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'enrollment_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'exam_roll': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'group': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.Section']", 'null': 'True', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['school.Subject']", 'null': 'True', 'blank': 'True'})
        },
        'school.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'coordinator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Faculty']"}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"})
        },
        'school.department': {
            'Meta': {'object_name': 'Department'},
            'hod': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hod'", 'to': "orm['profiles.Faculty']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"})
        },
        'school.school': {
            'Meta': {'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'school_type': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'school.section': {
            'Meta': {'object_name': 'Section'},
            'batch': ('django.db.models.fields.IntegerField', [], {}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['school.Course']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"})
        },
        'school.session': {
            'Meta': {'object_name': 'Session'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'school.subject': {
            'Meta': {'object_name': 'Subject'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"})
        }
    }

    complete_apps = ['mentor_system']