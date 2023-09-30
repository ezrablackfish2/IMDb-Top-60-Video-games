from rest_framework import serializers, permissions
from django.contrib.auth import get_user_model

from .models import (VideoGame,
        Video,
        Review,
        Rating,
        WatchList, 
        Photo,
        Trivia,
        Goof,
        Quote,
        FrequentlyAskedQuestion,
        ParentsGuide,
        Help,
        SoundTrack,
        Cast,
        CastVideo, 
        CastPhoto,
        CastTrivia,
        CastGoof,
        CastQuote,
        CastSalary,
        CastTrademark,
        CastFaqs,
        Platform,
        Genre,
        Thumbnail,
)

class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ('thumbnail',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre',)

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('platform',)


class GameListSerializer(serializers.ModelSerializer):
    genra = GenreSerializer(many=True, read_only=True)
    platform = PlatformSerializer(many=True, read_only=True)
    class Meta:
        fields = (
                "id",
                "title",
                "cover",
                "release_date",
                "year",
                "imdb_rating",
                "metascore",
                "certificate",
                "platform",
                "genra",
        )
        model = VideoGame

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video',)

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('photo',)

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = ('username', 'review',)

class RatingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Rating
        fields = ('username', 'your_rating',)
    def to_representation(self, instance):
        if self.context['request'].user.is_authenticated:
            user = self.context['request'].user
            if instance.user == user:
                return super().to_representation(instance)
        return None

class WatchListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = WatchList
        fields = ('username', 'your_watchlist',)
    def to_representation(self, instance):
        if self.context['request'].user.is_authenticated:
            user = self.context['request'].user
            if instance.user == user:
                return super().to_representation(instance)
        return None

class TriviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trivia
        fields = ('trivia',)

class GoofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goof
        fields = ('goof',)

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('quote',)

class FrequentlyAskedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestion
        fields = ('faq',)

class ParentsGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentsGuide
        fields = ('certification',)

class ParentalGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentsGuide
        fields = (
                'certification',
                'nudity',
                'violence',
                'profanity',
                'drugs',
                'intense_scene',
                )

class HelpListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('general_information',)

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ('cover', 'name', 'role')

class SoundTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundTrack
        fields = ('soundtracks',)

class CastPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastPhoto
        fields = ('castphoto',)

class CastVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastVideo
        fields = ('castvideo',)

class CastTriviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastTrivia
        fields = ('casttrivia',)

class CastGoofSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastGoof
        fields = ('castgoof',)

class CastQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastQuote
        fields = ('castquote',)

class CastSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CastSalary
        fields = ('castsalary',)

class CastTrademarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastTrademark
        fields = ('casttrademark',)

class CastFaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastFaqs
        fields = ('castfaq',)

class CastDetailSerializer(serializers.ModelSerializer):
    castphotos = CastPhotoSerializer(many=True, read_only=True)
    castvideos = CastVideoSerializer(many=True, read_only=True)
    casttrivias = CastTriviaSerializer(many=True, read_only=True)
    castquotes = CastQuoteSerializer(many=True, read_only=True)
    casttrademarks = CastTrademarkSerializer(many=True, read_only=True)
    castsalaries = CastSalarySerializer(many=True, read_only=True)
    castfaqs = CastFaqsSerializer(many=True, read_only=True)
    castgoofs = CastGoofSerializer(many=True, read_only=True)

    class Meta:
        model = Cast
        fields = (
                'id',
                'name',
                'cover',
                'starmeter' ,
                'bio',
                'award',
                'castphotos',
                'castvideos',
                'officialsite',
                'nickname',
                'Height',
                'born',
                'spouses',
                'children',
                'parents',
                'relatives',
                'country_of_origin',
                'language',
                'casttrivias',
                'castgoofs',
                'castquotes',
                'casttrademarks',
                'castsalaries',
                'castfaqs',
        )

class GameDetailSerializer(serializers.ModelSerializer):
    parentalguides = ParentalGuideSerializer(many=True, read_only=True)
    thumbnail = ThumbnailSerializer(many=True, read_only=True)
    genra = GenreSerializer(many=True, read_only=True)
    platform = PlatformSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    casts = CastSerializer(many=True, read_only=True)
    soundtracks = SoundTrackSerializer(many=True, read_only=True)
    class Meta:
        model = VideoGame
        fields = (
                'id',
                "title",
                "year",
                "cover",
                "thumbnail",
                "imdb_rating",
                "metascore",
                "popularity",
                "sold",
                "storyline",
                "director",
                "writer",
                "award",
                "platform",
                "videos",
                "photos",
                "casts",
                "genre",
                "genra",
                "certificate",
                "parentalguides",
                "trivias",
                "quotes",
                "goofs",
                "soundtracks",
                "reviews",
                "faqs",
                "release_date",
                "country_of_origin",
                "officialsite",
                "language",
                "nickname",
                "company",
                "color",
                "soundmix",
        )

    reviews = ReviewSerializer(many=True, read_only=True)
    trivias = TriviaSerializer(many=True, read_only=True)
    goofs = GoofSerializer(many=True, read_only=True)
    quotes = QuoteSerializer(many=True, read_only=True)
    faqs = FrequentlyAskedQuestionSerializer(many=True, read_only=True)

class GameDetailSignedSerializer(serializers.ModelSerializer):
    parentalguides = ParentalGuideSerializer(many=True, read_only=True)
    thumbnail = ThumbnailSerializer(many=True, read_only=True)
    genra = GenreSerializer(many=True, read_only=True)
    platform = PlatformSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    watchlists = WatchListSerializer(many=True, read_only=True)
    casts = CastSerializer(many=True, read_only=True)
    soundtracks = SoundTrackSerializer(many=True, read_only=True)
    class Meta:
        model = VideoGame
        fields = (
                "id",
                "title",
                "year",
                "cover",
                "thumbnail",
                "imdb_rating",
                "ratings",
                "watchlists",
                "metascore",
                "popularity",
                "storyline",
                "director",
                "writer",
                "award",
                "platform",
                "videos",
                "photos",
                "casts",
                "genra",
                "certificate",
                "parentalguides",
                "trivias",
                "quotes",
                "goofs",
                "soundtracks",
                "reviews",
                "faqs",
                "release_date",
                "country_of_origin",
                "officialsite",
                "language",
                "nickname",
                "company",
                "color",
                "soundmix",
        )

    reviews = ReviewSerializer(many=True, read_only=True)
    trivias = TriviaSerializer(many=True, read_only=True)
    goofs = GoofSerializer(many=True, read_only=True)
    quotes = QuoteSerializer(many=True, read_only=True)
    faqs = FrequentlyAskedQuestionSerializer(many=True, read_only=True)

class GameListSignedSerializer(serializers.ModelSerializer):
    genra = GenreSerializer(many=True, read_only=True)
    platform = PlatformSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    watchlists = WatchListSerializer(many=True, read_only=True)
    class Meta:
        fields = (
                "id",
                "title",
                "cover",
                "release_date",
                "year",
                "imdb_rating",
                "metascore",
                "certificate",
                "platform",
                "genra",
                "ratings",
                "watchlists",
        )
        model = VideoGame
