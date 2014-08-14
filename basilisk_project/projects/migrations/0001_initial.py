# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Repo'
        db.create_table(u'projects_repo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('repo_type', self.gf('django.db.models.fields.CharField')(default='git', max_length=3)),
            ('repo_url', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'projects', ['Repo'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('repo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Repo'])),
        ))
        db.send_create_signal(u'projects', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Repo'
        db.delete_table(u'projects_repo')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')


    models = {
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'repo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Repo']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'projects.repo': {
            'Meta': {'object_name': 'Repo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repo_type': ('django.db.models.fields.CharField', [], {'default': "'git'", 'max_length': '3'}),
            'repo_url': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['projects']