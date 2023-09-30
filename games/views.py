from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect


from .models import (
        VideoGame,
        Help,
        Rating,
        WatchList,
        Review,
        Cast,
        Video,
        SoundTrack,
        Photo,
        Trivia,
        Goof,
        Quote,
        FrequentlyAskedQuestion,
        ParentsGuide,
        CastVideo,
        CastPhoto,
        CastTrivia,
        CastGoof,
        CastQuote,
        CastSalary,
        CastTrademark,
        CastFaqs,
)
from .serializers import (
        GameListSerializer,
        GameDetailSerializer,
        HelpListSerializer,
        GameDetailSignedSerializer,
        GameListSignedSerializer,
        RatingSerializer,
        ReviewSerializer,
        WatchListSerializer,
        CastSerializer,
        CastDetailSerializer,
        VideoSerializer,
        PhotoSerializer,
        TriviaSerializer,
        GoofSerializer,
        QuoteSerializer,
        FrequentlyAskedQuestionSerializer,
        ParentalGuideSerializer,
        SoundTrackSerializer,
        CastPhotoSerializer,
        CastVideoSerializer,
        CastTriviaSerializer,
        CastGoofSerializer,
        CastQuoteSerializer,
        CastSalarySerializer,
        CastTrademarkSerializer,
        CastFaqsSerializer,
)

# Create your views here.
class GameList(generics.ListAPIView):
    def get_queryset(self):
        queryset = VideoGame.objects.all().order_by('-imdb_rating')
        return queryset
    
    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return GameListSignedSerializer
        else:
            return GameListSerializer

class GameDetail(generics.RetrieveAPIView):
    queryset = VideoGame.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return GameDetailSignedSerializer
        else:
            return GameDetailSerializer

class GameRate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        game_id = self.kwargs['videogame_id']
        user = self.request.user
        try:
            rating = Rating.objects.get(game_id=game_id, user=user)
        except Rating.DoesNotExist:
            game = get_object_or_404(VideoGame, id=game_id)
            rating = Rating.objects.create(game=game, user=user)

        return rating

    def delete(self, request, *args, **kwargs):
        rating = self.get_object()
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GameWatchList(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        game_id = self.kwargs['videogame_id']
        user = self.request.user

        try:
            watchlist = WatchList.objects.get(game_id=game_id, user=user)
        except WatchList.DoesNotExist:
            game = get_object_or_404(VideoGame, id=game_id)
            watchlist = WatchList.objects.create(game=game, user=user)

        return watchlist

class GameReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        game_id = self.kwargs['videogame_id']
        user = self.request.user

        try:
            review = Review.objects.get(game_id=game_id, user=user)
        except Review.DoesNotExist:
            game = get_object_or_404(VideoGame, id=game_id)
            review = Review.objects.create(game=game, user=user)

        return review

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HelpList(generics.ListCreateAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpListSerializer

class SearchResultsListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = VideoGame.objects.all()
        title = self.request.query_params.get('title', None)
        writer = self.request.query_params.get('writer', None)
        director = self.request.query_params.get('director', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if writer:
            queryset = queryset.filter(writer__icontains=writer)
        if director:
            queryset = queryset.filter(director__icontains=director)

        return queryset

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return GameListSignedSerializer
        else:
            return GameListSerializer

class CastList(generics.ListAPIView):
    serializer_class = CastSerializer

    def get_queryset(self):
        # Get the VideoGame object based on the video game id captured from the URL
        video_game_id = self.kwargs['videogame_id']
        video_game = VideoGame.objects.get(id=video_game_id)

        return Cast.objects.filter(game=video_game)

class CastDetail(generics.RetrieveAPIView):
    queryset = Cast.objects.all() 
    serializer_class = CastDetailSerializer
    lookup_field = 'id'

class About(generics.ListAPIView):
    pass

class Contact(generics.ListAPIView):
    pass

class VideoList(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        video_game_id = self.kwargs['videogame_id']
        video_game = VideoGame.objects.get(id=video_game_id)

        return Video.objects.filter(game=video_game)

class PhotoList(generics.ListAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        video_game_id = self.kwargs['videogame_id']
        video_game = VideoGame.objects.get(id=video_game_id)

        return Photo.objects.filter(game=video_game)

class TriviaList(generics.ListAPIView):
    serializer_class = TriviaSerializer

    def get_queryset(self):
        video_game_id = self.kwargs['videogame_id']
        video_game = VideoGame.objects.get(id=video_game_id)

        return Trivia.objects.filter(game=video_game)

class ParentalGuideList(generics.ListAPIView):
    serializer_class = ParentalGuideSerializer

    def get_queryset(self):
        video_game_id = self.kwargs['videogame_id']
        video_game = VideoGame.objects.get(id=video_game_id)

        return ParentsGuide.objects.filter(game=video_game)

class GoofList(generics.ListAPIView):
    serializer_class = GoofSerializer

    def get_queryset(self):
        video_game_id = self.kwargs['videogame_id']
        video_game = VideoGame.objects.get(id=video_game_id)

        return Goof.objects.filter(game=video_game)

class QuoteList(generics.ListAPIView):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        video_game_id = self.kwargs['videogame_id']
        video_game = VideoGame.objects.get(id=video_game_id)

        return Quote.objects.filter(game=video_game)

class SoundTrackList(generics.ListAPIView):
    serializer_class = SoundTrackSerializer

    def get_queryset(self):
        video_game_id = self.kwargs['videogame_id']
        video_game = VideoGame.objects.get(id=video_game_id)

        return SoundTrack.objects.filter(game=video_game)

class FAQList(generics.ListAPIView):
    serializer_class = FrequentlyAskedQuestionSerializer

    def get_queryset(self):
        video_game_id = self.kwargs['videogame_id']
        video_game = VideoGame.objects.get(id=video_game_id)

        return FrequentlyAskedQuestion.objects.filter(game=video_game)

class CastVideoList(generics.ListAPIView):
    serializer_class = CastVideoSerializer

    def get_queryset(self):
        cast_id = self.kwargs['cast_id']
        cast = Cast.objects.get(id=cast_id)

        return CastVideo.objects.filter(game=cast)

class CastPhotoList(generics.ListAPIView):
    serializer_class = CastPhotoSerializer

    def get_queryset(self):
        cast_id = self.kwargs['cast_id']
        cast = Cast.objects.get(id=cast_id)

        return CastPhoto.objects.filter(game=cast)

class CastTriviaList(generics.ListAPIView):
    serializer_class = CastTriviaSerializer

    def get_queryset(self):
        cast_id = self.kwargs['cast_id']
        cast = Cast.objects.get(id=cast_id)

        return CastTrivia.objects.filter(game=cast)

class CastGoofList(generics.ListAPIView):
    serializer_class = CastGoofSerializer

    def get_queryset(self):
        cast_id = self.kwargs['cast_id']
        cast = Cast.objects.get(id=cast_id)

        return CastGoof.objects.filter(game=cast)

class CastQuoteList(generics.ListAPIView):
    serializer_class = CastQuoteSerializer

    def get_queryset(self):
        cast_id = self.kwargs['cast_id']
        cast = Cast.objects.get(id=cast_id)

        return CastQuote.objects.filter(game=cast)

class CastSalaryList(generics.ListAPIView):
    serializer_class = CastSalarySerializer

    def get_queryset(self):
        cast_id = self.kwargs['cast_id']
        cast = Cast.objects.get(id=cast_id)

        return CastSalary.objects.filter(game=cast)

class CastTrademarkList(generics.ListAPIView):
    serializer_class = CastTrademarkSerializer

    def get_queryset(self):
        cast_id = self.kwargs['cast_id']
        cast = Cast.objects.get(id=cast_id)

        return CastTrademark.objects.filter(game=cast)

class CastFaqsList(generics.ListAPIView):
    serializer_class = CastFaqsSerializer

    def get_queryset(self):
        cast_id = self.kwargs['cast_id']
        cast = Cast.objects.get(id=cast_id)

        return CastFaqs.objects.filter(game=cast)

