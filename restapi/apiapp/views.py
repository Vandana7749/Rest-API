
from urllib import request, response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import colstudentSerializer
from .models import colstudent 

@api_view(['GET', 'POST'])
def getdata(request):
    if request.method == 'GET':
        emp = colstudent.objects.all()
        serializer = colstudentSerializer(emp, many=True)
        return Response(serializer.data)
        '''
        return Response({
        'status':1, 
        'message':'Hello There! get',
        'Method':'GET'
        })
        '''
    elif request.method == 'POST':
        return Response({
        'status':2, 
        'message':'Hello There Post',
        'Method':'Post'
        })
    else:
        return("You called an invalid method    ")    

@api_view(['POST'])   
def postdata(request):
    try: 
        data = request.data
        serializer = colstudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            print(data)
            return Response("Successfully added.")
        
        return Response({
            "data" : serializer.errors,
            "message" : "provide the missing data"})
        
    except Exception as e:
        print(e)
        return Response("Something went wrong.")




