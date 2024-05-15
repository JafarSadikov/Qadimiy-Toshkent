from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FileBook

from django.core.exceptions import ValidationError


class FileDownload(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file_instance = FileBook.objects.get(id=pk)
        except FileBook.DoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        file_instance.downloads += 1
        file_instance.save()

        if file_instance.file:
            file_url = request.build_absolute_uri(file_instance.file.url)
            response = {
                "path": file_url
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            raise ValidationError("No file associated with this FileBook instance.")


