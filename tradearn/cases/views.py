from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
# from push_notifications.models import GCMDevice

class ListAllCases(APIView):

    def get(self, request, format=None):

        # device = GCMDevice.objects.get(registration_id='c4ArjjbVD5Y:APA91bGAnX_6kZ-w7txOm6w2YEBjlSwFno79PO6FES2BuDk9G4NgYAXM2Y-t6qA9ptEqgxVDUpKMxGlBwK7qKbZsl_CPVAjc_SUw0oyLKp95zgRIsYcApFBU-C95kgvJ1Ykr6eoZlK3i')
        # print(device)
        # device.send_message(None, extra={"foo": "bar"})

        user = request.user
        
        all_cases = models.Case.objects.filter(owner__username=user)

        serializer = serializers.CaseSerializer(all_cases, many=True, context={'request': request})

        """
        Serializer로 serialize할 때, 동일한 모델을 serialize하는 serializer를 사용해야만 함.
        
        여기서, all_cases는 models.Case이고,
        CaseSerialize 역시 models.Case를 씨리얼라이즈하고 있으(serializer.py참조)므로 가능
        """

        return Response(data=serializer.data)

class UploadCases(APIView):

    def post(self, request, format=None):

        user = request.user

        serializer = serializers.CaseUploadSerializer(data=request.data)


        if serializer.is_valid():

            serializer.save(owner=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadsCases(APIView):

    def post(self, request, format=None):

        user = request.user

        serializer = serializers.CasesUploadSerializer(data=request.data)


        if serializer.is_valid():

            serializer.save(owner=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)