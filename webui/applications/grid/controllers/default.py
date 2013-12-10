# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
from drama import Drama

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return "HELLO WORLD"
    #return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def analyse():
    files = db.files
    session_name = files.session_name
    q= session_name==session.session_id
    s = db(q)
    rows = s.select()
    groups={}
    #group managment
    for r in rows:
        if r.groupname not in groups:
            groups[r.groupname]=[]
            tmpfile = {}
            tmpfile["filename"] = r.filename
            tmpfile["address"] = request.folder+"uploads/"+r.doc
            tmpfile2 = {}
            tmpfile2["name"] = "whole"
            tmpfile2["address"] = "no-address"
            tmpfile2["stats"] = {"group":"0"}
            groups[r.groupname].append(tmpfile)
            groups[r.groupname].append(tmpfile2)
        else:
            tmpfile = {}
            tmpfile["filename"] = r.filename
            tmpfile["address"] = r.doc
            groups[r.groupname].append(tmpfile)
    #for every group we go through the files
    values = groups.viewvalues()
    for g in values:
        for text in g:
            if (text["address"] != "no-address"):
                drama = Drama(text["address"])
                text["bible_name"] = drama.get_bibl_title()
                text["name"] = drama.get_title()
                text["stats"] = drama.get_speech_length_info()
    return dict(session_id=session.session_id,answer=groups)

def upload_file():
    try:
        f = request.vars['files[]']
        id = db.files.insert(doc = db.files.doc.store(f.file, f.filename))
        record = db.files[id]
        path_list = []
        path_list.append(request.folder)
        path_list.append('uploads')
        path_list.append(record['doc'])
        File = db(db.files.id==id).select()[0]
        namearray = f.filename.split(".")
        tmpfilename = namearray[1]+".xml"
        tmpgorupname = namearray[0]
        sessionname = session.session_id
        db.files[id] = dict(filename=tmpfilename)
        db.files[id] = dict(groupname=tmpgorupname)
        db.files[id] = dict(session_name=sessionname)
        res = dict(files=[{"name": str(f.filename), "url": URL(f='download', args=[File['doc']]), "delete_url": URL(f='delete_file', args=[File['doc']]), "delete_type": "DELETE" }])
        return res
    except:
        return dict(message=T('Upload error'))

def delete_file():
        """
        Delete an uploaded file
        """
        try:
            name = request.args[0]
            db(db.files.doc==name).delete()
            return dict(message=T('File deleted'))
        except:
            return dict(message=T('Deletion error'))


def upload():
        session.session_id = response.session_id
        return dict(session_id=session.session_id)