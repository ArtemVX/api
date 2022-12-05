from rest_framework import generics


from meetups.models import MeetUp
from meetups.serializers import MeetUpSerializer


class MeetUpAPIList(generics.ListCreateAPIView):
    queryset = MeetUp.objects.all()
    serializer_class = MeetUpSerializer


# class MeetUpAPIView(APIView):
#
#     def get(self, request):
#         meetups = MeetUp.objects.all()
#         return Response({'meetups': MeetUpSerializer(meetups, many=True).data})
#
#     def post(self, request):
#         serializer = MeetUpSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)   # проверка корректности и вывод исключений
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = MeetUp.objects.get(pk=pk)
#         except:
#             return Response({"error": "Method PUT not allowed"})
#
#         serializer = MeetUpSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         # удаление записи
#
#         return Response({"post": "delete post " + str(pk)})
#

