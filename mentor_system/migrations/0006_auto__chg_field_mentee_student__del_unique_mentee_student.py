# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Mentee', fields ['student']
        db.delete_unique('mentors_mentee', ['student_id'])


        # Changing field 'Mentee.student'
        db.alter_column('mentors_mentee', 'student_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Student']))

    def backwards(self, orm):

        # Changing field 'Mentee.student'
        db.alter_column('mentors_mentee', 'student_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['profiles.Student'], unique=True))
        # Adding unique constraint on 'Mentee', fields ['student']
        db.create_unique('mentors_mentee', ['student_id'])


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
        'mentors.mentee': {
            'Meta': {'object_name': 'Mentee'},
            'additional_information': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'degree_board': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'degree_division': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'degree_remarks': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'degree_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'emergency_location': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'emergency_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'emergency_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family_member1_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family_member1_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family_member1_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family_member1_relationship': ('django.db.models.fields.CharField', [], {'default': "'Father'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'family_member2_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family_member2_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family_member2_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family_member2_relationship': ('django.db.models.fields.CharField', [], {'default': "'Father'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'family_member3_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family_member3_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family_member3_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family_member3_relationship': ('django.db.models.fields.CharField', [], {'default': "'Father'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'family_member4_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family_member4_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family_member4_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family_member4_relationship': ('django.db.models.fields.CharField', [], {'default': "'Father'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'family_member5_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'family_member5_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'family_member5_qualification': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'family_member5_relationship': ('django.db.models.fields.CharField', [], {'default': "'Father'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inter_board': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'inter_division': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'inter_remarks': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'inter_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'interests': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'local_guardian_address': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'local_guardian_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'local_guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'local_guardian_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'others_board': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'others_division': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'others_remarks': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'others_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'permanent_address_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'permanent_address_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'permanent_address_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'permanent_address_pincode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'permanent_address_state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'permanent_address_street': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'present_address_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'present_address_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'present_address_phone': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'present_address_pincode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'present_address_state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'present_address_street': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'school_board': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'school_division': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'school_remarks': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'school_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'special_achievements': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Student']"})
        },
        'mentors.menteemeeting': {
            'Meta': {'object_name': 'MenteeMeeting'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentors.Mentee']"}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mentors.Mentor']"}),
            'remarks': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'mentors.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'faculty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Faculty']"}),
            'group': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.Section']"})
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

    complete_apps = ['mentors']