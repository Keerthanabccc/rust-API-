from django.shortcuts import render


from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response




# Create your views here.





class new(APIView):
    def post(self,request):
        a=newserializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data)




    def get(self,request):
        aq=news.objects.all()
        a=newserializer(aq,many=True)
        return Response(a.data)






# using id
class newdetail(APIView):
    def get(self,request,**kwargs):
        new=news.objects.get(id=kwargs.get('pk'))
        a=newserializer(new)
        return Response(a.data)










class hotelview(APIView):
    def post(self,request):
        b=hotelserializer(data=request.data)
        if b.is_valid():
            b.save()
        return Response(b.data)





    def get(self,request):
        pq=hotels.objects.all()
        b=hotelserializer(pq,many=True)
        return Response(b.data)




# usind id

class hotdetail(APIView):
    def put(self,request,**kwargs):
        hot=hotels.objects.get(id=kwargs.get('sk'))
        m=hotelserializer(hot)
        return Response(m.data)


from rest_framework import generics
from rest_framework import mixins


class productview(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = productform
    queryset = productmodel.objects.all()
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)





# using id

class prody(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = productmodel.objects.all()
    serializer_class = productform
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)









from rest_framework import status
from rest_framework import viewsets



class todoviewsets(viewsets.ViewSet):
    serializer_class=viewserial
    model=viewmodel


    def list(self,request):
        a=self.model.objects.all()
        b=self.serializer_class(a,many=True)
        return Response(b.data,status=status.HTTP_200_OK)


    def create(self,request):
        a=self.serializer_class(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data,status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)




    def update(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        b=self.serializer_class(data=request.data,instance=a)
        if b.is_valid():
            b.save()
            return Response(b.data,status=status.HTTP_201_CREATED)
        else:
            return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)




    def retrieve(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        b=self.serializer_class(a)
        return Response(b.data,status=status.HTTP_200_OK)



    def destroy(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        a.delete()
        return Response({"msg":"deleted"},status=status.HTTP_200_OK)


















class newyviewsets(viewsets.ViewSet):
    serializer_class=newyserial
    model=newywmodel


    def list(self,request):
        a=self.model.objects.all()
        b=self.serializer_class(a,many=True)
        return Response(b.data,status=status.HTTP_200_OK)


    def create(self,request):
        a=self.serializer_class(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data,status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)




    def update(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        b=self.serializer_class(data=request.data,instance=a)
        if b.is_valid():
            b.save()
            return Response(b.data,status=status.HTTP_201_CREATED)
        else:
            return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)




    def retrieve(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        b=self.serializer_class(a)
        return Response(b.data,status=status.HTTP_200_OK)



    def destroy(self,request,**kwargs):
        a=self.model.objects.get(id=kwargs.get('pk'))
        a.delete()
        return Response({"msg":"deleted"},status=status.HTTP_200_OK)





class personview(viewsets.ModelViewSet):
    serializer_class=personserial
    queryset=personmodel.objects.all()







from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def empview(request):
    if(request.method=='GET'):
        a=todosmodel.objects.all()
        b=todoserializer(a,many=True)
        return Response(b.data)
    if(request.method=='POST'):
        a=todoserializer(data=request.data)
        if a.is_valid():
            a.save()
            return Response(a.data,status=status.HTTP_201_CREATED)
        else:
            return Response(a.errors,status=status.HTTP_400_BAD_REQUEST)










@api_view(['GET','PUT','DELETE'])
def emplodet(request,id):
    if(request.method=='GET'):
        a=todosmodel.objects.get(id=id)
        b=todoserializer(a)
        return Response(b.data)

    if(request.method=='PUT'):
        a=todosmodel.objects.get(id=id)
        b=todoserializer(instance=a,data=request.data)
        if b.is_valid():
            b.save()
            return Response(b.data)
        else:
            return Response({'msg':'updation failed'})

        if(request.method=='DELETE'):
            a=todosmodel.objects.get(id=id)
            a.delete()
            return Response({'msg':'data deleted'})