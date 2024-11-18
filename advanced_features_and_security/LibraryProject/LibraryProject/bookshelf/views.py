from django.shortcuts import render

# Create your views here.
#Create groupe 
from django.contrib.auth.models import Group , Permission
from django.contrib.contenttypes.models import ContentType
from .models import User

Editors, created = Group.objects.get_or_create(name='Editors')
Viewers, created = Group.objects.get_or_create(name='Viewers')
Admins, created = Group.objects.get_or_create(name='Admins')


ct = ContentType.objects.get_for_model(User)

can_view = Permission.objects.create(name='can_view')
can_create = Permission.objects.create(name='can_create')
can_edit = Permission.objects.create(name='can_edit')
can_delete = Permission.objects.create(name='can_delete')


Viewers.permissions.add(can_view)
Editors.permissions.add(can_view,can_edit)
Admins.permissions.add(can_view,can_edit,can_create,can_delete)

from django.contrib.auth.decorators import permission_required

@permission_required('advanced_features_and_security.can_view')
def can_view(request):
    pass

@permission_required("advanced_features_and_security.can_create")
def can_create(request):
    pass

@permission_required("advanced_features_and_security.can_edit")
def can_edit(request):
    pass

@permission_required("advanced_features_and_security.can_delete")
def can_delete(request):
    pass
