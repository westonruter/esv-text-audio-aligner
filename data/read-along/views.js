

var ChapterView = Backbone.View.extend({
    initialize: function(){
        this.render()
    },
    render: function(){
        var vars = {
            title: 'Unknown',
            text: 'lorem ipsum'
        };
        var template = _.template( $("#chapter_template").html(), vars );
        this.el.html( template );
    },
    open: function(book, chapter){
        console.info('Opening: '+ book + '.' + chapter)
    }
});

var chapter_view = new ChapterView({
    el: $("#chapter_view")
});

var QueryView = Backbone.View.extend({
    initialize: function(){
        this.render()
    },
    render: function(){
        var vars = {
            books: ESVBible.map(function(book){ return {
                text: book.get('name'),
                value: book.get('osis')
            }})
        };
        var template = _.template( $("#query_template").html(), vars );
        this.el.html( template );
        this.$('#book')[0].selectedIndex = -1;
        this.$('#chapter').val('');
    },
    

    selectBook: function(book){
        if( book == this.$('#book').val() ){
            return;
        }
        this.$('#book').val(book).trigger('change');
    },
    selectChapter: function(chapter){
        if( chapter == this.$('#chapter').val() ){
            return;
        }
        this.$('#chapter').val(chapter);
    },
    
    events: {
        "submit form"   : "onSubmitForm",
        "change #book"  : "onChangeBook"
    },
    
    onSubmitForm: function(e){
        e.preventDefault();
        var book = this.$('#book').val();
        var chapter = this.$('#chapter').val();
        if( !book || !chapter ){
            alert("Oops! Your browser shouldn't have let you submit the form. You're missing values.");
            return;
        }
        app_router.navigate(book + '.' + chapter, true);
    },
    
    onChangeBook: function(e){
        var book = this.$('#book').val();
        var bookObj = _.first(ESVBible.select(function(bookObj){ return book == bookObj.get('osis'); }));
        var $chapter = this.$('#chapter');
        $chapter.attr('max', bookObj.get('chapters'));
        $chapter.val( Math.min($chapter.val(), bookObj.get('chapters')) );
    }
    
});

var query_view = new QueryView({
   el: $("#query_view")
});
