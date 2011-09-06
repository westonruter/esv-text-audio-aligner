

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
                value: book.get('value')
            }})
        };
        var template = _.template( $("#query_template").html(), vars );
        ESVBible.each(function(book){
            
        })
        this.el.html( template );
    }
});

var query_view = new QueryView({
   el: $("#query_view")
});
