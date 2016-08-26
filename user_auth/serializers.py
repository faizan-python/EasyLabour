from rest_framework import serializers

from EasyLabour.non_null_serializer import BaseSerializer
from user_auth.models import User


class UserSerializer(BaseSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'id', 'password', 'email',
            'full_name', 'phone_number', 'country_code', 'role',
            'first_name', 'last_name', 'middle_name')
        read_only_fields = ('id', 'password',)

    def create(self, validated_data):
        first_name = validated_data.get('first_name', '')
        middle_name = validated_data.get('middle_name', '')
        last_name = validated_data.get('last_name', '')
        full_name = ''
        if first_name:
            full_name = first_name
        if middle_name:
            full_name = full_name + middle_name
        if last_name:
            full_name = full_name + last_name
        if not full_name:
            full_name = validated_data.get('full_name', '')



        user = User.objects.create(
                phone_number=validated_data['phone_number'],
                first_name = first_name,
                middle_name = middle_name,
                last_name = last_name,
                full_name=full_name,
                role=validated_data['role'],
                is_active=True
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
