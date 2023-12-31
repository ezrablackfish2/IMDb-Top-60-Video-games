from django.urls import path

from .views import (
        GameList,
        GameDetail,
        HelpList,
        GameRate,
        GameWatchList,
        GameReview,
        SearchResultsListView,
        CastList,
        CastDetail,
        About,
        Contact,
        PhotoList,
        VideoList,
        TriviaList,
        ParentalGuideList,
        GoofList,
        QuoteList,
        SoundTrackList,
        FAQList,
        CastTriviaList,
        CastVideoList,
        CastPhotoList,
        CastGoofList,
        CastQuoteList,
        CastSalaryList,
        CastTrademarkList,
        CastFaqsList,

)

urlpatterns = [
        path("", GameList.as_view(), name="game_list"),
        path("<uuid:pk>/", GameDetail.as_view(), name="game_detail"),
        path("<uuid:videogame_id>/casts/", CastList.as_view(), name="cast_list"),
        path("<uuid:videogame_id>/casts/<uuid:id>/", CastDetail.as_view(), name="cast_detail"),
        path("<uuid:videogame_id>/casts/<uuid:cast_id>/trivia/", CastTriviaList.as_view(), name="cast_trivia_list"),
        path("<uuid:videogame_id>/casts/<uuid:cast_id>/video/", CastVideoList.as_view(), name="cast_trivia_list"),
        path("<uuid:videogame_id>/casts/<uuid:cast_id>/photo/", CastPhotoList.as_view(), name="cast_trivia_list"),
        path("<uuid:videogame_id>/casts/<uuid:cast_id>/goof/", CastGoofList.as_view(), name="cast_trivia_list"),
        path("<uuid:videogame_id>/casts/<uuid:cast_id>/salary/", CastSalaryList.as_view(), name="cast_trivia_list"),
        path("<uuid:videogame_id>/casts/<uuid:cast_id>/trademark/", CastTrademarkList.as_view(), name="cast_trivia_list"),
        path("<uuid:videogame_id>/casts/<uuid:cast_id>/faq/", CastFaqsList.as_view(), name="cast_trivia_list"),
        path("<uuid:videogame_id>/rating/", GameRate.as_view(), name="game_rating"),
        path("<uuid:videogame_id>/watchlist/", GameWatchList.as_view(), name="game_watchlist"),
        path("<uuid:videogame_id>/review/", GameReview.as_view(), name="game_review"),
        path("<uuid:videogame_id>/video/", VideoList.as_view(), name="video_list"),
        path("<uuid:videogame_id>/photo/", PhotoList.as_view(), name="photo_list"),
        path("<uuid:videogame_id>/trivia/", TriviaList.as_view(), name="trivia_list"),
        path("<uuid:videogame_id>/certificate/", ParentalGuideList.as_view(), name="certificate_list"),
        path("<uuid:videogame_id>/goof/", GoofList.as_view(), name="goof_list"),
        path("<uuid:videogame_id>/quote/", QuoteList.as_view(), name="quote_list"),
        path("<uuid:videogame_id>/soundtrack/", SoundTrackList.as_view(), name="soundtrack_list"),
        path("<uuid:videogame_id>/faq/", FAQList.as_view(), name="faq_list"),
        path("search/", SearchResultsListView.as_view(), name="search_results"),
        path("help/", HelpList.as_view(), name="help"),
        path("about/", About.as_view(), name="about"),
        path("contact/", Contact.as_view(), name="contact"),
]
