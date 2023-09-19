# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from django.views import View
from rest_framework import viewsets

from rest_framework.generics import GenericAPIView

from django.shortcuts import render, HttpResponse, redirect
from .models import Blog, Bloguser,Blogdetails,Resume ,Student,Mark,Interest,City,Person,PersonAddress
import re 
from django.db.models import Q ,Count ,Avg,Sum, Aggregate
from .serializers import *

from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.views import APIView


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,authentication_classes

from rest_framework.mixins import ListModelMixin,CreateModelMixin

class Genericcity(ListModelMixin,CreateModelMixin,GenericAPIView):

    queryset=City.objects.all()
    serializer=cityserializer

    def get(self,request, *args, **kwargs):
        self.list(request, *args, **kwargs)

@authentication_classes([ TokenAuthentication]==True)
@permission_classes([IsAuthenticated]==True)
class Relationship(View):
    def get(self, request):
        #Blog.objects.values_list('id', 'name')
        persondata = Person.objects.get(id=2)
        print(persondata.interests.all())
        for interest in persondata.interests.all():
            print(interest, '**********')
        #print(persondata.query)

        address=persondata.personaddress
        print(address.city, address.street_address)
        return render(request, 'index.html')
        return HttpResponse(persondata.interests)
        
        #columns
       
class Resumeblog(viewsets.ModelViewSet):
     queryset = Resume.objects.all() 
     serializer_class = ResumeSerializer 
     
    # def get(self, request):
    #     queryset = Resume.objects.all() 
    #     serializer_class = ResumeSerializer 

    #     #return JsonResponse("testing " ,safe=False)
    #     return Response({

    #     })

    # def post(self,request):
    #      return  Response({
            
    #     })

class Blogapi(APIView):
    #serializerclass=Newblogserializer
    def get(self, request):
        blogs = Blog.objects.all()
        #columns
        blogsdata = Blog.objects.all().values_list('id','BlogName','user')[1:5]
        print('one', blogsdata.query)
        blogfilter = Blog.objects.all().filter(Image='' , BlogName='', user=1).values_list('id')
        bloglast3records = Blog.objects.order_by('-id').values()[3]
        print(bloglast3records)


        #group by example
        blogsgroup = Blog.objects.values('BlogName').annotate(head_count=Count('id'))
        #print('group',blogsgroup)
        #print('group',blogsgroup.query)

        #having clause in django orm
        bloguserdetails=Blog.objects.values('BlogName').annotate(head_count=Count(Bloguser)).filter(head_count__gt=1)
        #print(bloguserdetails)
        #print(bloguserdetails.query)
        
        #marks

        #marksquery=Mark.objects.select_related('student').all().aggregate(sum('marks'))
        #marksquery=Student.objects.select_related('mark').all().values_list('id', 'marks', 'student', 'student_id', 'subject_id').values('student').all().annotate(Sum('marks'),Count('subject_id'))
        marksquery=Student.objects.select_related('mark').all().values('Studentname', 'id', 'mark').all().annotate(Sum('mark'),Count('id'))
        
        print(marksquery.query)

        #print(blogsdata)
        #print(blogfilter)
        departments_serializer = BlogSerializer(blogs, many=True)
        #return Response(departments_serializer.data)
        return Response({"Message":"Success","blogdata":departments_serializer.data})
    
    def post(self, request):
        print("request",request.data)
        serializerblog=BlogDetailsSerializer(data=request.data)
        print(request.data)
        if serializerblog.is_valid():
           print("ifffff")
           serializerblog.save()
           #departments = Blogdetails.objects.create(id=request.data["BlogDeatilsID"],BlogName=request.data["BlogName"] ,Description=request.data["Description"]   )
           #deprecords=Blogdetails.objects.all().filter(id=request.data["BlogDeatilsID"]).values()
           return JsonResponse("Added Successfully!!" , safe=False)
           return Response({"Message":"Success","blogdata":deprecords})
        else:
             print("elseeee")
             return Response({"Message":"Failed","blogdata":serializerblog.errors})

@authentication_classes([ TokenAuthentication]==True)
@permission_classes([IsAuthenticated]==True)
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = Bloguser.objects.all() 
    serializer_class = BlogUserSerializer  

  
class CustomAuthTokenLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user'] 
        #user = serializer.validated_data['Bloguser']  
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': user.username ,
            'password': user.password
        })

def homepage(request):
        
 # email = request.session.get('email'){'userdetails': blogusers}
   blogdata = Blog.objects.all()

   context={
        'Blog':blogdata
   }


   return render(request, 'blog.html', context ) 



def readblogdata(request,id):
        
 # email = request.session.get('email'){'userdetails': blogusers}
   oneblogdata = Blog.objects.get(id=id)

   context={
        'Blog':oneblogdata
   }


   return render(request, 'oneblog.html', context ) 

def dashboard(request):
        
    email = request.session.get('email')

    mydata2 = Bloguser.objects.get(Email=email)

    blogdata = Blog.objects.filter(user=mydata2)

    print(blogdata)

    logindata={
        'name':mydata2,
        'bloginfo':blogdata
        
    }

    print(logindata)
    #return HttpResponse(mydata2)

    return render(request, 'Dashboardblog.html', logindata) 


def addblog(request):

    email = request.session.get('email')

    mydata2 = Bloguser.objects.get(Email=email)

    logindata={
        'name':mydata2,
        
    }

    return render(request, 'addDashboard.html',logindata ) 
     

@permission_classes((IsAuthenticated))
@api_view(['GET'])
def  checkpermission(request):  
    if request.method=='GET': 
         return JsonResponse("checked  Successfully!!" , safe=False)


@api_view(['POST'])    
def  insertblog(request): 
    
    if request.method=='POST': 
        email = request.session.get('email')

        mydata2 = Bloguser.objects.get(Email=email)
        try:
            resdata=request.data
            print(resdata['blog'], resdata['img'], resdata['desc'])
            blogdata=Blog.objects.create(BlogName=resdata['blog'] ,Image=resdata['img'] ,
                        Description= resdata['desc'] ,user=mydata2  )
            Blogserializer=BlogSerializer(blogdata, many=False)
            return redirect(dashboard)
            # return JsonResponse("successfully done",safe=False) 
        
        except Exception as e:
               return HttpResponse(e)  
          


def updateblog(request):

    email = request.session.get('email')

    mydata2 = Bloguser.objects.get(Email=email)

    blogId = request.GET['id']

    blogdata = Blog.objects.get(id=blogId) 

    context={
        'name':mydata2,
        'oneblogdata': blogdata
        
    }

    context1 = {
        'oneblogdata': blogdata
    }

    return render(request, 'editblog.html', context)

           

def  editBlog(request,id): 
       
       email = request.session.get('email')

       mydata2 = Bloguser.objects.get(Email=email)
       
       if request.method == 'POST':

        BlogName = request.POST['blog']
        desc = request.POST['desc']
        img = request.POST['img']
       

        blogrecord = Blog(
            id=id, BlogName=BlogName, Description=desc,  Image=img ,user=mydata2 )
        blogrecord.save()


        return redirect(dashboard)


#@api_view(['DELETE'])    
def deleteblog(request):
    
    blogdelete = request.GET['id']

    department=Blog.objects.get(id=blogdelete)
    department.delete()
    return redirect(dashboard)




def adduser(request):
      if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        
        password = request.POST['password']
        
        existinguserrecord= Bloguser.objects.filter(Email=email).count()
        
        if existinguserrecord<1 :
            userrecord = Bloguser(
                Name=username, Email=email, Password=password )
            userrecord.save()

            ID = userrecord.id

            print('record user insert', ID)

            messages.success(request, 'You have Succesfully Registred , Login Now  '  )

            return redirect(homepage) 
      
        else:
             return HttpResponse("ALready EMAIL IS REGISTERD , Try with Different Email")


def login(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        request.session['email'] = email
        request.session['password'] = password

        if email!='':
             
            try:
                userlogin = Bloguser.objects.filter(
                    Q(Email=email) & Q(Password=password))
                if (userlogin):
                    return redirect('/blog/dashboard')
                    return HttpResponse("suucess")
                else:
                    print("not valid")
                    messages.success(request, 'entered email or password is In Correct')
                    return redirect('/blog/login')
                    

            except Exception as e:
                return HttpResponse(e)
                pass

        else:

             return HttpResponse ('Not valid')
        

    else:
 
          return render (request,'bloglogin.html')



def register(request):
	 return render(request ,"blogregister.html")



def logout(request):
 
 try:
        del request.session['email']
        del request.session['password']
 except:
        pass
 return HttpResponse("<h1>Thank you for staying in ,  you have logged out successfully</h1>")



# class HelloView(APIView):  ,Image=resdata['img'] ,Description= resdata['desc']
# 	permission_classes = (IsAuthenticated, )

# 	def get(self, request):
# 		content = {'message': 'Hello, GeeksforGeeks'}
# 		return Response(content)
