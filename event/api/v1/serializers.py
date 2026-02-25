from rest_framework import serializers
from event.models import Event, EventAgenda, EventLearning, EventUniversity

# --- Nested serializers ---
class EventAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAgenda
        fields = ('id', 'agenda_item')

class EventLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLearning
        fields = ('id', 'content')

class EventUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUniversity
        fields = ('id', 'universities')

# --- Event serializer ---
class EventSerializer(serializers.ModelSerializer):
    agendas = EventAgendaSerializer(many=True, read_only=True)
    learnings = EventLearningSerializer(many=True, read_only=True)
    universities = EventUniversitySerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = (
            'id', 'title', 'description', 'icon', 'location', 'date', 'time',
            'image', 'slug', 'category', 'created_at', 'updated_at',
            'agendas', 'learnings', 'universities'
        )

