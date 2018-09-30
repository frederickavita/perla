# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
POST_PAR_PAGE = 30


def test():
    return locals()

def erreur():
    return "page erreur"


def get_categorie():
    nom_categorie = request.args(0)
    categorie = db.produit(url=nom_categorie)
    if not categorie:
        redirect(URL('erreur'))
    return categorie


def caftan_en_location():
    print(session.cart)
    Position= T("Position")
    Name = T("Nom")
    Price = T("Prix")
    locat = T("Caftan en location")
    perpage = T("Par page")
    caftans = db(db.produit.types == locat).select()
    page = request.args(1, cast=int, default=0)
    start = page * POST_PAR_PAGE
    stop = start + POST_PAR_PAGE
    caftansnoms = db(db.produit.types == locat).select(orderby=~db.produit.nom,  limitby=(start, stop))
    caftansdates = db(db.produit.types == locat).select(orderby=~db.produit.id, limitby=(start, stop))
    caftansprixs = db(db.produit.types == locat).select(orderby=~db.produit.prix_total, limitby=(start, stop))
    print(len(caftansnoms))
    print("sdsdsds")
    Featured_Collection = T("Collections Flash")
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom, limitby=(0, 5) )
    rows = db(db.produit.id > 0).select()
    last_row = rows.last()
    fear = last_row['id']
    if fear > 1 and fear <= 9  :
        chiffre = 9
    elif fear > 9 and fear <= 15:
        chiffre = 15
    elif  fear > 15 :
        chiffre = 30
    else:
        pass
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return locals()

def caftan_en_vente():
    Position= T("Position")
    Name = T("Nom")
    Price = T("Prix")
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom, limitby=(0, 5))
    rows = db(db.produit.id > 0).select()
    last_row = rows.last()
    fear = last_row['id'] 
    print(fear)
    if fear > 1 and fear <= 9  :
        chiffre = 9
    elif fear > 9 and fear <= 15:
        chiffre = 15
    elif  fear > 15 :
        chiffre = 30
    else:
        pass
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    locat = "Caftan en vente"
    page = request.args(1, cast=int, default=0)
    start = page * POST_PAR_PAGE
    stop = start + POST_PAR_PAGE
    caftansnoms = db(db.produit.types == locat).select(orderby=~db.produit.nom, limitby=(start, stop))
    caftansdates = db(db.produit.types == locat).select(orderby=~db.produit.id, limitby=(start, stop))
    caftansprixs = db(db.produit.types == locat).select(orderby=~db.produit.prix_total,limitby=(start, stop))
    return locals()

def robe_de_soiree_en_location():
    Position= T("Position")
    Name = T("Nom")
    Price = T("Prix")
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom, limitby=(0, 5))
    rows = db(db.produit.id > 0).select()
    last_row = rows.last()
    fear = last_row['id']
    if fear > 1 and fear <= 9  :
        print(fear)
        print("kkkk")
        chiffre = 9
    elif fear > 9 and fear <= 15:
        chiffre = 15
    elif  fear > 15 :
        chiffre = 30
    else:
        chiffre = 0
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    locat = "Robe de soirée en location"
    page = request.args(1, cast=int, default=0)
    start = page * POST_PAR_PAGE
    stop = start + POST_PAR_PAGE
    caftansnoms = db(db.produit.types == locat).select(orderby=~db.produit.nom, limitby=(start, stop))
    caftansdates = db(db.produit.types == locat).select(orderby=~db.produit.id, limitby=(start, stop))
    caftansprixs = db(db.produit.types == locat).select(orderby=~db.produit.prix_total, limitby=(start, stop))
    return locals()


def robe_de_soiree_en_vente():
    Sort= T("TRIEZ PAR")
    Position= T("Position")
    Name = T("Nom")
    Price = T("Prix")
    locat = T("Caftan en location")
    perpage = T("Par page")
    Featured_Collection = T("Collections Flash")
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom)
    rows = db(db.produit.id > 0).select()
    last_row = rows.last()
    fear = last_row['id']
    if fear > 1 and fear <= 9  :
        print(fear)
        print("kkkk")
        chiffre = 9
    elif fear > 9 and fear <= 15:
        chiffre = 15
    elif  fear > 15 :
        chiffre = 30
    else:
        chiffre = 0
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    locat = "Robe de soirée en vente"
    page = request.args(1, cast=int, default=0)
    start = page * POST_PAR_PAGE
    stop = start + POST_PAR_PAGE
    caftansnoms = db(db.produit.types == locat).select(orderby=~db.produit.nom, limitby=(start, stop))
    caftansdates = db(db.produit.types == locat).select(orderby=~db.produit.id,limitby=(start, stop))
    caftansprixs = db(db.produit.types == locat).select(orderby=~db.produit.prix_total, limitby=(start, stop))
    return locals()


def caftan_blanche():
    Position= T("Position")
    Name = T("Nom")
    Price = T("Prix")
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom)
    rows = db(db.produit.id > 0).select()
    last_row = rows.last()
    fear = last_row['id']
    if fear > 1 and fear <= 9  :
        print(fear)
        print("kkkk")
        chiffre = 9
    elif fear > 9 and fear <= 15:
        chiffre = 15
    elif  fear > 15 :
        chiffre = 30
    else:
        chiffre = 0
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    locat = "Caftan blanche"
    page = request.args(1, cast=int, default=0)
    start = page * POST_PAR_PAGE
    stop = start + POST_PAR_PAGE
    caftansnoms = db(db.produit.types == locat).select(orderby=~db.produit.nom, limitby=(start, stop))
    caftansdates = db(db.produit.types == locat).select(orderby=~db.produit.id, limitby=(start, stop))
    caftansprixs = db(db.produit.types == locat).select(orderby=~db.produit.prix_total, limitby=(start, stop))
    return locals()

def djelleba():
    Position= T("Position")
    Name = T("Nom")
    Price = T("Prix")
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom, limitby=(0, 5))
    rows = db(db.produit.id > 0).select()
    last_row = rows.last()
    fear = last_row['id']
    if fear > 1 and fear <= 9  :
        print(fear)
        print("kkkk")
        chiffre = 9
    elif fear > 9 and fear <= 15:
        chiffre = 15
    elif  fear > 15 :
        chiffre = 30
    else:
        chiffre = 0
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    locat = "Djellaba"
    page = request.args(1, cast=int, default=0)
    start = page * POST_PAR_PAGE
    stop = start + POST_PAR_PAGE
    caftansnoms = db(db.produit.types == locat).select(orderby=~db.produit.nom,limitby=(start, stop))
    caftansdates = db(db.produit.types == locat).select(orderby=~db.produit.id,limitby=(start, stop))
    caftansprixs = db(db.produit.types == locat).select(orderby=~db.produit.prix_total,limitby=(start, stop))
    return locals()

def Guandoura():
    Position= T("Position")
    Name = T("Nom")
    Price = T("Prix")
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom)
    rows = db(db.produit.id > 0).select()
    last_row = rows.last()
    fear = last_row['id']
    if fear > 1 and fear <= 9  :
        print(fear)
        print("kkkk")
        chiffre = 9
    elif fear > 9 and fear <= 15:
        chiffre = 15
    elif  fear > 15 :
        chiffre = 30
    else:
        chiffre = 0
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    locat = "Guandoura"
    page = request.args(1, cast=int, default=0)
    start = page * POST_PAR_PAGE
    stop = start + POST_PAR_PAGE
    caftansnoms = db(db.produit.types == locat).select(orderby=~db.produit.nom,limitby=(start, stop))
    caftansdates = db(db.produit.types == locat).select(orderby=~db.produit.id,limitby=(start, stop))
    caftansprixs = db(db.produit.types == locat).select(orderby=~db.produit.prix_total,limitby=(start, stop))
    return locals()

def bijoux():
    Position= T("Position")
    Name = T("Nom")
    Price = T("Prix")
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom)
    rows = db(db.produit.id > 0).select()
    last_row = rows.last()
    fear = last_row['id']
    if fear > 1 and fear <= 9  :
        print(fear)
        print("kkkk")
        chiffre = 9
    elif fear > 9 and fear <= 15:
        chiffre = 15
    elif  fear > 15 :
        chiffre = 30
    else:
        chiffre = 0
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    locat = "Bijoux"
    page = request.args(1, cast=int, default=0)
    start = page * POST_PAR_PAGE
    stop = start + POST_PAR_PAGE
    caftansnoms = db(db.produit.types == locat).select(orderby=~db.produit.nom,limitby=(start, stop))
    caftansdates = db(db.produit.types == locat).select(orderby=~db.produit.id,limitby=(start, stop))
    caftansprixs = db(db.produit.types == locat).select(orderby=~db.produit.prix_total,limitby=(start, stop))
    return locals()

def acceuil():
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom,limitby=(0, 5) )
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return locals()

def apropos():
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom,limitby=(0, 5) )
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return locals()

def devente():
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom,limitby=(0, 5) )
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return locals()

def delocation():
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom,limitby=(0, 5) )
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return locals()

def securite():
    caftans =  db().select(db.produit.ALL, orderby=db.produit.nom,limitby=(0, 5) )
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return locals()

def suppr():
    db.produit.truncate()
    db.produit.drop()
    return locals()


def contact():
    form = SQLFORM(db.contact)
    if form.process().accepted:
        response.flash = "Formulaire accepter"
    elif form.errors:
        response.flash = ""
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return locals()



def vue():
    print(URL('default', 'acceuil'))
    id = request.args(0)
    print(id)
    caftans = db(db.produit.url == id).select()
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
    elif form3.errors:
        response.flash = ""
    return locals()


def enregistrement():
    form = auth.register()
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
        redirect(URL('profile'))
    elif form3.errors:
        response.flash = ""
    return locals()


def login():
    form=auth.login()
    form3 = SQLFORM(db.newsletter)
    if form3.process(hideerror=True).accepted:
        response.flash = "Formulaire accepter"
        redirect(URL('profile'))
    elif form3.errors:
        response.flash = ""
    return locals()



# an action to add and remove items from the shopping cart
def cart_callback():
    id = int(request.vars.id)
    if request.vars.action == 'add':
        session.cart[id]=session.cart.get(id,0)+1
    if request.vars.action == 'sub':
        session.cart[id]=max(0,session.cart.get(id,0)-1)
    return str(session.cart[id])

@auth.requires_login()
def utilisateur():
    ret = db(db.auth_user.id == me).select()
    print(ret)
    user = User(a0 or me)
    print(user)
    if not user:
        redirect(URL('login'))
    return locals()


def profile():
    if not auth.user:
        redirect('acceuil')
    form=auth.profile()
    return locals()


def mylog():
    return dict(form=auth.login())






def checksession():
    for k, v in session.cart.items():
        if session.cart[k] == 0:
            del session.cart[k]
    



def panier():
    print(session.cart)
    vide = False
    close = ".close"
    closing = "close"
    head = ".cart-header"
    heading = "cart-header"
    if not session.cart:
        vide = True
    produits = db().select(db.produit.ALL, orderby=db.produit.nom) 
    #for product_id, qty in session.cart.iteritems():
    #    produits = db(db.produit.id == product_id).select()
    #    quantite = qty
    #    print(qty)
    return locals()



def gratuit():
    id = request.vars.name
    print(id)
    id = int(id[0])
    a = "#"
    c = a  + str(id)
    session.cart[id]=session.cart.get(id,0)+1
    return "Enregistrement"





def reduire():
    print("ggggggg")
    id = request.vars.red
    id = int(id[0])
    a = "#"
    c = a  + str(id)
    session.cart[id]=max(0,session.cart.get(id,0)-1)
    print("bbbbb")
    return "supprimer"




def commande():
    if not auth.user:
        redirect('login')
    livraison = db(db.livraison.users ==me).select()
    facturation = db(db.facturation.users ==me).select()
    db.livraison.users.default = me
    form = SQLFORM(db.livraison)
    if form.process().accepted:
        response.flash = 'your comment is posted'
    elif form.errors:
        response.flash = 'form has errors'    
    db.facturation.users.default = me
    record = me
    db.livraison.id.readable=False 
    form2 = SQLFORM(db.livraison, record, deletable=False,
                  upload=URL('download'))
    if form2.process().accepted:
       response.flash = 'form accepted'
    elif form2.errors:
       response.flash = 'form has errors'

    form1 = SQLFORM(db.facturation)
    return locals()








def testing():
    return locals()


def echo():
    import json
    if "cart" in request.vars:
        session.cart = json.loads(request.vars.cart)
        print(session.cart) 
        print("nnnnn") 




def russe():
    import json
    if "chiffre" in request.vars:
        session.chiffre = json.loads(request.vars.chiffre)
        print(session.chiffre) 
        print("zzzzzzzzz")     



def nettoyage():
    if "nettoyage" in request.vars:
        session.cart = None
        print(session.cart)





def faire():
    print(request.vars.value)
    print("xcxwcxwcxwcwx")


def paiement():
    import time
    import datetime
    if not session.cart:
        redirect('panier')
    pk=STRIPE_PUBLISHABLE_KEY
    user = User(a0 or me)
    email = user.email
    security_notice = True
    disclosure_notice = True
    signature  = 123456789
    ids = ''
    livraison = db(db.livraison.users ==me).select()    
    produit = session.cart
    chiffre = session.chiffre 
    montantthtx = chiffre['montanthtx']
    tva = chiffre['tva']
    quantite = chiffre['quantite']
    ret = chiffre['livraison']
    total = chiffre['total']
    return locals()


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())



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
