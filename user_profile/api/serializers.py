from rest_framework import serializers
from user_profile.models import Contact



class ContactSerializer(serializers.ModelSerializer):
    # last_updated_api = serializers.DateTimeField(read_only=True, format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Contact
        fields = '__all__'
        # read_only_fields = ['status']

    def validate_name(self, value):
        value = ' '.join(value.split()).title()
        return value

    def validate_last_name(self, value):
        if value is not None:
            value = ' '.join(value.split()).title()
            return value
