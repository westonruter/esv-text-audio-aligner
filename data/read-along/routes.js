

var AppRouter = Backbone.Router.extend({
    routes: {
        ":bookCode.:chapterNumber": "viewChapter"
    },
    viewChapter: function(bookCode, chapterNumber){
        chapterNumber = parseInt(chapterNumber, 10);
        
        query_view.selectBook(bookCode);
        query_view.selectChapter(chapterNumber);
        
        var bookObj = _(esv_bible.select(function(bookObj){ return bookObj.get('osis') == bookCode; })).first();
        var chapter = new Chapter({
            book: bookObj,
            number: chapterNumber
        });
        
        chapter_view.model = chapter;
        chapter_view.render();
    }
});
var app_router = new AppRouter();

document.addEventListener('DOMContentLoaded', function(){
    Backbone.history.start();
}, true);


