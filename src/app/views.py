from django.shortcuts import render_to_response
from app.models import contact,contact_phone
from django.db.models import Q
from django.http import HttpResponse

def home(request):
    "***Default Page WebSite***"
    _contact=contact_phone.objects.all().select_related('contact').order_by('contact__name')
    return render_to_response("home.html",{'title':'AddressBook','contact':_contact})
    
def search(request):
    "***Search Page WebSite***"
    if  ('q' in request.GET and request.GET['q'])  and ('type' in request.GET and request.GET['type']):
        name=request.GET['q']
        _type=request.GET['type']
        _contact=contact_phone.objects.all().select_related('contact').\
        filter(Q(contact__name__icontains=name)|Q(contact__family__icontains=name),contact__typecontact=_type)
        return render_to_response("home.html",{'title':'AddressBook','contact':_contact,'search':name})
    else:
        return render_to_response("home.html",{'title':'AddressBook','contact':None})
def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)
def insert(request):
    result=None
    if ('name' in request.GET and request.GET['name'])  and ('family' in request.GET and request.GET['family']) and \
        ('gender' in request.GET and request.GET['gender'])  and ('typecontact' in request.GET and request.GET['typecontact']):
        _name=request.GET['name']
        _type=request.GET['typecontact']
        _gender=request.GET['gender']
        _family=request.GET['family']
        contact.objects.create(name=_name,family=_family,gender=_gender,typecontact=_type);
        result="add new contact"
    elif ('id' in request.GET and request.GET['id'])  and ('phone' in request.GET and request.GET['phone']):
        _Fkid=request.GET['id']
        _phone=request.GET['phone']
        contact_phone.objects.create(phone=_phone,contact_id=_Fkid)
        result="add new phone"
    else:
        result=("Eror"*3)
        
      
    _contact=contact.objects.all()
    
    
    return render_to_response("insert.html",{'title':'insert page','result':result,"contact":_contact})
