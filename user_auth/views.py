from django.shortcuts import render
from django.views.generic import View
from rest_framework import generics, permissions, status


class RegisterView(generics.GenericAPIView):
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'status': -1,
                'errors': serializer.errors,
            })
        user = authenticate(
            username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key
            })
        return Response({
            'error': 'Invalid Credentials'
        }, status=status.HTTP_400_BAD_REQUEST)