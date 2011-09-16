var NotificationView = Backbone.View.extend({
    collection: null,
    initialize: function(){
        //this.notifications.create({message:'fp'})
        var view = this;
        
        this.collection.bind("add", function(notification){
            view.el.prop('hidden', false);
            var item = _.template( $("#notification_template").html(), {
                cid: notification.cid,
                message: notification.get('message'),
                type: notification.get('type')
            });
            view.el.prepend(item);
        });
        
        this.collection.bind("remove", function(notification){
            view.el.find('[data-cid="' + notification.cid + '"]').remove();
            if(this.isEmpty()){
                view.el.prop('hidden', true);
            }
        });
        
        this.render();
    },
    render: function(){
        // This needs to list out all from the Notification collection
    },
    events: {
        "click .notification": "clickItem"
    },
    clickItem: function(e){
        var notification = this.collection.getByCid($(e.target).data('cid'));
        this.collection.remove(notification);
    }
});
var notification_view = new NotificationView({
    el: $('#notification_view'),
    collection: notifications
});


var ChapterView = Backbone.View.extend({
    model: Chapter, // ???
    
    initialize: function(){
        
    },
    render: function(){
        var vars = {
            title: this.model.get('book').get('name') + ' ' + this.model.get('number')
        };
        var template = _.template( $("#chapter_template").html(), vars );
        this.el.html( template );
        var view = this;
        this.model.loadData(function(responseData){
            if(responseData.errors.length){
                _(responseData.errors).each(function(error){
                    notifications.add({message: error.toString(), type:"error"});
                });
                view.$('.text').html('');
            }
            else {
                view.$('.text').html(responseData.text);
            }
        });
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
            books: esv_bible.map(function(book){ return {
                text: book.get('name'),
                value: book.get('osis')
            }})
        };
        var template = _.template( $("#query_template").html(), vars );
        this.el.html( template );
        this.$('#book')[0].selectedIndex = -1;
        this.$('#chapter').val('');
    },
    

    selectBook: function(osisBook){
        if( osisBook == this.$('#book').val() ){
            return;
        }
        this.$('#book').val(osisBook).trigger('change');
    },
    selectChapter: function(chapterNumber){
        if( chapterNumber == this.$('#chapter').val() ){
            return;
        }
        this.$('#chapter').val(chapterNumber);
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
        var bookObj = _.first(esv_bible.select(function(bookObj){ return book == bookObj.get('osis'); }));
        var $chapter = this.$('#chapter');
        $chapter.attr('max', bookObj.get('chapters'));
        $chapter.val( Math.min($chapter.val(), bookObj.get('chapters')) );
    }
    
});

var query_view = new QueryView({
   el: $("#query_view")
});
