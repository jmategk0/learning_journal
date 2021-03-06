from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPFound
from .forms import EntryCreateForm

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    Entry,
    )

"""
@view_config(route_name='home', renderer='string')
def index_page(request):
    return 'list page'
"""
@view_config(route_name='home', renderer='templates/list.jinja2')
def index_page(request):
    entries = Entry.all()
    return {'entries': entries}

@view_config(route_name='detail', renderer='templates/detail.jinja2')
def view(request):
    this_id = request.matchdict.get('id', -1)
    entry = Entry.by_id(this_id)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry}

@view_config(route_name='action', match_param='action=create', renderer='templates/edit.jinja2')
def create(request):
    entry = Entry()
    form = EntryCreateForm(request.POST)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        DBSession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}

@view_config(route_name='action', match_param='action=edit', renderer='string')
def update(request):
    return 'edit page'
'''

    http://localhost:6543/
    http://localhost:6543/journal/1
    http://localhost:6543/journal/create
    http://localhost:6543/journal/edit
'''
