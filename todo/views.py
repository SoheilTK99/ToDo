from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets


#region function base view
@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = ToDo.objects.order_by('priority').all()
        todo_serializer = ToDoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def todo_detail_view (request: Request, todo_id:int):
    try:
        todo = ToDo.objects.get(pk=todo_id)
    except ToDo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilizer = ToDoSerializer(todo)
        return Response(serilizer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        serilizer = ToDoSerializer(todo, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT) 

# endregion   

#region classbase view 
class ToDosListApiView(APIView):
    def get(self, request:Request):
        todos = ToDo.objects.order_by('priority').all()
        todo_serializer = ToDoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    def post(self, request:Request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)    

class ToDosDetailApiView(APIView):

    def get_object(self, todo_id: int):
        try:
            todo = ToDo.objects.get(pk=todo_id)
            return todo
        except ToDo.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)        

    def get(self, request:Request, todo_id:int):
        todo = self.get_object(todo_id)
        serilizer = ToDoSerializer(todo)
        return Response(serilizer.data, status.HTTP_200_OK)        

    def put(self, request:Request, todo_id:int):
        todo = self.get_object(todo_id)
        serilizer = ToDoSerializer(todo, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)       

    def delete(self, request:Request, todo_id:int):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)       
#endregion

#region mixin
class ToDosListMixinApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ToDo.objects.order_by('priority').all()
    serializer_class = ToDoSerializer

    def get(self, request:Request):
        return self.list(request)
    
    def post(self, request:Request):
        return self.create(request)
    

class ToDosDetailMixinApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ToDo.objects.order_by('priority').all()
    serializer_class = ToDoSerializer   

    def get(self, request:Request, pk):
        return self.retrieve(request, pk)    

    def put(self, request:Request, pk):
        return self.update(request, pk)

    def delete(self, request:Request, pk):
        return self.destroy(request, pk)  

#endregion

#region grneric

class ToDoGenericApiView(generics.ListCreateAPIView):
    queryset = ToDo.objects.order_by('priority').all()
    serializer_class = ToDoSerializer    


class ToDoGenericDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.order_by('priority').all()
    serializer_class = ToDoSerializer 

#endregion

#region viewset

class ToDosViewsetApiView(viewsets.ModelViewSet):
    queryset = ToDo.objects.order_by('priority').all()
    serializer_class = ToDoSerializer     

#endregion



