# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


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

def upload_file():
        """
        File upload handler for the ajax form of the plugin jquery-file-upload
        Return the response in JSON required by the plugin
        """
        try:
            # Get the file from the form
            f = request.vars['files[]']
            # Store file on the server
            id = db.files.insert(doc = db.files.doc.store(f.file, f.filename))
            record = db.files[id]
            path_list = []
            path_list.append(request.folder)
            path_list.append('uploads')
            path_list.append(record['doc'])
	    #set the filename variable.
	    #set the groupname variable.
	    #nameing convention groupname.filename.xml
	    res = ""
	    namearray = f.filename.split(".")
	    if(len(namearray)<4):
	    	tmpfilename = namearray[1]+".xml"
		tmpgorupname = namearray[0]
	    	db.files[id] = dict(filename=tmpfilename)
		db.files[id] = dict(groupname=tmpgorupname)
		res = tmpfilename + ", " + tmpgorupname
	    else:
		res = "filename must be groupname.filename.xml"
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
        return dict()
