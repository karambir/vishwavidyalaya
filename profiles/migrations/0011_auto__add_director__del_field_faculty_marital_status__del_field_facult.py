# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Director'
        db.create_table('profiles_director', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empID', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.School'])),
        ))
        db.send_create_signal('profiles', ['Director'])

        # Deleting field 'Faculty.marital_status'
        db.delete_column('profiles_faculty', 'marital_status')

        # Deleting field 'Faculty.is_mentor'
        db.delete_column('profiles_faculty', 'is_mentor')

        # Deleting field 'Faculty.is_admin'
        db.delete_column('profiles_faculty', 'is_admin')

        # Adding field 'Faculty.department'
        db.add_column('profiles_faculty', 'department',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['school.Department']),
                      keep_default=False)


        # Renaming column for 'Faculty.school' to match new field type.
        db.rename_column('profiles_faculty', 'school', 'school_id')
        # Changing field 'Faculty.school'
        db.alter_column('profiles_faculty', 'school_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.School']))
        # Adding index on 'Faculty', fields ['school']
        db.create_index('profiles_faculty', ['school_id'])

        # Deleting field 'Student.address_city'
        db.delete_column('profiles_student', 'address_city')

        # Deleting field 'Student.address_street'
        db.delete_column('profiles_student', 'address_street')

        # Deleting field 'Student.alternate_phone'
        db.delete_column('profiles_student', 'alternate_phone')

        # Deleting field 'Student.enrolment_number'
        db.delete_column('profiles_student', 'enrolment_number')

        # Deleting field 'Student.address_state'
        db.delete_column('profiles_student', 'address_state')

        # Deleting field 'Student.address_pincode'
        db.delete_column('profiles_student', 'address_pincode')

        # Adding field 'Student.enrollment_number'
        db.add_column('profiles_student', 'enrollment_number',
                      self.gf('django.db.models.fields.CharField')(max_length=15, unique=True, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Student.course'
        db.alter_column('profiles_student', 'course_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Course']))

        # Changing field 'Student.section'
        db.alter_column('profiles_student', 'section_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['school.Section'], null=True))

    def backwards(self, orm):
        # Removing index on 'Faculty', fields ['school']
        db.delete_index('profiles_faculty', ['school_id'])

        # Deleting model 'Director'
        db.delete_table('profiles_director')

        # Adding field 'Faculty.marital_status'
        db.add_column('profiles_faculty', 'marital_status',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=30),
                      keep_default=False)

        # Adding field 'Faculty.is_mentor'
        db.add_column('profiles_faculty', 'is_mentor',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Faculty.is_admin'
        db.add_column('profiles_faculty', 'is_admin',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Faculty.department'
        db.delete_column('profiles_faculty', 'department_id')


        # Renaming column for 'Faculty.school' to match new field type.
        db.rename_column('profiles_faculty', 'school_id', 'school')
        # Changing field 'Faculty.school'
        db.alter_column('profiles_faculty', 'school', self.gf('django.db.models.fields.CharField')(max_length=300))
        # Adding field 'Student.address_city'
        db.add_column('profiles_student', 'address_city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.address_street'
        db.add_column('profiles_student', 'address_street',
                      self.gf('django.db.models.fields.CharField')(max_length=350, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.alternate_phone'
        db.add_column('profiles_student', 'alternate_phone',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.enrolment_number'
        db.add_column('profiles_student', 'enrolment_number',
                      self.gf('django.db.models.fields.CharField')(unique=True, max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.address_state'
        db.add_column('profiles_student', 'address_state',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.address_pincode'
        db.add_column('profiles_student', 'address_pincode',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Student.enrollment_number'
        db.delete_column('profiles_student', 'enrollment_number')


        # Changing field 'Student.course'
        db.alter_column('profiles_student', 'course_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['academics.Course']))

        # Changing field 'Student.section'
        db.alter_column('profiles_student', 'section_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['academics.Section']))

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
        'profiles.director': {
            'Meta': {'object_name': 'Director'},
            'empID': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
        'school.subject': {
            'Meta': {'object_name': 'Subject'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['school.School']"})
        }
    }

    complete_apps = ['profiles']