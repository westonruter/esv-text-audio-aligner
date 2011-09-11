

var AppRouter = Backbone.Router.extend({
    routes: {
        ":book.:chapter": "viewChapter"
    },
    viewChapter: function(book, chapter){
        query_view.selectBook(book);
        query_view.selectChapter(chapter);
        chapter_view.open(book, chapter);
    }
});
var app_router = new AppRouter();

document.addEventListener('DOMContentLoaded', function(){
    Backbone.history.start();
}, true);


