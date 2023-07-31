from django.contrib import admin

# Register your models here.
from .models import (
        VideoGame, 
        Review, 
        Video, 
        Photo, 
        Trivia, 
        Goof, 
        Quote, 
        FrequentlyAskedQuestion, 
        ParentsGuide, 
        Rating, 
        WatchList, 
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
)

class WatchListInLine(admin.TabularInline):
    model = WatchList

class RatingInLine(admin.TabularInline):
    model = Rating

class ReviewInLine(admin.TabularInline):
    model = Review

class PhotoInLine(admin.TabularInline):
    model = Photo

class TriviaInLine(admin.TabularInline):
    model = Trivia

class GoofInLine(admin.TabularInline):
    model = Goof

class QuoteInLine(admin.TabularInline):
    model = Quote

class FAQInLine(admin.TabularInline):
    model = FrequentlyAskedQuestion

class ParentsGuideInLine(admin.StackedInline):
    model = ParentsGuide

class VideoInLine(admin.StackedInline):
    model = Video

class SoundTrackInLine(admin.StackedInline):
    model = SoundTrack

class CastPhotoInLine(admin.StackedInline):
    model = CastPhoto

class CastVideoInLine(admin.StackedInline):
    model = CastVideo

class CastTriviaInLine(admin.StackedInline):
    model = CastTrivia

class CastGoofInLine(admin.StackedInline):
    model = CastGoof

class CastQuoteInLine(admin.StackedInline):
    model = CastQuote


class CastSalaryInLine(admin.StackedInline):
    model = CastSalary 

class CastTrademarkInLine(admin.StackedInline):
    model = CastTrademark

class CastFaqsInLine(admin.StackedInline):
    model = CastFaqs


class CastInLine(admin.StackedInline):
    model = Cast
    fields = ("cover", "name", "role")

class CastAdmin(admin.ModelAdmin):
    fields = (
            'name',
            'cover',
            'starmeter',
            'bio',
            'award',
            'officialsite',
            'nickname',
            'Height',
            'born',
            'country_of_origin',
            'language',
            'spouses',
            'children',
            'parents',
            'relatives',
    )

    inlines = [
            CastVideoInLine,
            CastPhotoInLine,
            CastTriviaInLine,
            CastQuoteInLine,
            CastTrademarkInLine,
            CastSalaryInLine,
            CastFaqsInLine,
    ]
    list_display = ("name", "id", "cover", "born","game",)

class GameAdmin(admin.ModelAdmin):
    fields = [
                "title",
                "cover",
                "metascore",
                "popularity",
                "sold",
                "storyline",
                "director",
                "writer",
                "award",
                "genre",
                "certificate",
                "release_date",
                "country_of_origin",
                "officialsite",
                "language",
                "nickname",
                "company",
                "color",
                "soundmix",
        ]
    inlines = [
            WatchListInLine,
            RatingInLine,
            VideoInLine,
            PhotoInLine,
            CastInLine,
            ParentsGuideInLine,
            TriviaInLine,
            GoofInLine,
            QuoteInLine,
            SoundTrackInLine,
            ReviewInLine,
            FAQInLine,
    ]
    list_display = ("title","id", "cover","certificate", "release_date", "imdb_rating",)

admin.site.register(VideoGame, GameAdmin)
admin.site.register(Help)
admin.site.register(Cast, CastAdmin)
