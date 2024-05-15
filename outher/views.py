from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, get_object_or_404, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from outher.models import About, Scientists, ElectronicBooks, Address
from outher.serializer import AboutSerializer, ScientistsSerializer, ElectronicBooksSerializer, ContactSerializer, \
    AddressSerializer, ElectronicBooksLikeSerializer


@api_view(['GET'])
def about_list(request):
    abouts = About.objects.all()
    serializer = AboutSerializer(abouts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def about_detail(request, pk):
    try:
        about = About.objects.get(pk=pk)
    except About.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AboutSerializer(about)
    return Response(serializer.data)


class ScientistListAPIView(ListAPIView):
    queryset = Scientists.objects.all().order_by("id")
    serializer_class = ScientistsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


@api_view(['GET'])
def scientist_detail(request, pk):
    try:
        scientist = Scientists.objects.get(pk=pk)
    except Scientists.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ScientistsSerializer(scientist)
    return Response(serializer.data)


class ElectronicListAPIView(ListAPIView):
    queryset = ElectronicBooks.objects.all().order_by("id")
    serializer_class = ElectronicBooksSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'file_books__title']
    permission_classes = [IsAuthenticated, ]


@api_view(['GET'])
def electronic_books_detail(request, pk):
    try:
        ebook = ElectronicBooks.objects.get(pk=pk)
    except ElectronicBooks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ElectronicBooksSerializer(ebook)
    return Response(serializer.data)


class ElectronicListLikeAPIView(RetrieveUpdateAPIView):
    queryset = ElectronicBooks.objects.all().order_by("id")
    serializer_class = ElectronicBooksLikeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if user.is_authenticated:
            existing_like = instance.users.filter(id=user.id).exists()
            if not existing_like:
                instance.users.add(user)
                instance.like += 1
            else:
                instance.users.remove(user)
                instance.like -= 1
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response({"error": "Foydalanuvchi avtorizatsiyadan o'tmagan"}, status=status.HTTP_401_UNAUTHORIZED)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ElectronicBooks, pk=pk)


class ContactListCreateView(APIView):

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def address_list_create(request):
    if request.method == 'GET':
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def address_edit(request, pk):
    try:
        address = Address.objects.get(pk=pk)
    except Address.DoesNotExist:
        return Response({"error": "Address not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)













