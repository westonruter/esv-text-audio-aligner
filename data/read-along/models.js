

var Book = Backbone.Model.extend({
    defaults: {
        name: "Unknown",
        osis: "unknown",
        chapters: 0
    },
    initialize: function(attributes){
        
    },
    getChapter: function(number){
        if(number <= 0 || number > this.attributes.chapters){
            throw Error("Chapter number out of range: " + number);
        }
        return new Chapter({
            book: this,
            number: number
        });
    }
});


var Chapter = Backbone.Model.extend({
    defaults: {
        book: null,
        number: 0
        /*,
        timings: [],
        html: null,
        audio: [] // list of URLs to audio
        */
    },
    audioFormats: [
        {
            'mime': 'audio/mpeg',
            'ext': 'mp3'
        },
        {
            'mime': 'audio/vnd.wave',
            'ext': 'wav'
        },
        {
            'mime': 'audio/ogg',
            'ext': 'ogg'
        }
    ],
    initialize: function( attributes ){
        
        
        
        
        // @todo Can this be async to fetch the html, audio urls
    }
    // Load html, audio, text, timings
    
});

var Bible = Backbone.Collection.extend({
    model: Book,
    toString: function(){
        return "Collection<Bible>";
    }
});

var ESVBible = new Bible([ // This array is generated via $ python bokinfo.py --js
    {
        "osis": "Gen", 
        "chapters": 50, 
        "name": "Genesis"
    }, 
    {
        "osis": "Exod", 
        "chapters": 40, 
        "name": "Exodus"
    }, 
    {
        "osis": "Lev", 
        "chapters": 27, 
        "name": "Leviticus"
    }, 
    {
        "osis": "Num", 
        "chapters": 36, 
        "name": "Numbers"
    }, 
    {
        "osis": "Deut", 
        "chapters": 34, 
        "name": "Deuteronomy"
    }, 
    {
        "osis": "Josh", 
        "chapters": 24, 
        "name": "Joshua"
    }, 
    {
        "osis": "Judg", 
        "chapters": 21, 
        "name": "Judges"
    }, 
    {
        "osis": "Ruth", 
        "chapters": 4, 
        "name": "Ruth"
    }, 
    {
        "osis": "1Sam", 
        "chapters": 31, 
        "name": "1 Samuel"
    }, 
    {
        "osis": "2Sam", 
        "chapters": 24, 
        "name": "2 Samuel"
    }, 
    {
        "osis": "1Kgs", 
        "chapters": 22, 
        "name": "1 Kings"
    }, 
    {
        "osis": "2Kgs", 
        "chapters": 25, 
        "name": "2 Kings"
    }, 
    {
        "osis": "1Chr", 
        "chapters": 29, 
        "name": "1 Chronicles"
    }, 
    {
        "osis": "2Chr", 
        "chapters": 36, 
        "name": "2 Chronicles"
    }, 
    {
        "osis": "Ezra", 
        "chapters": 10, 
        "name": "Ezra"
    }, 
    {
        "osis": "Neh", 
        "chapters": 13, 
        "name": "Nehemiah"
    }, 
    {
        "osis": "Esth", 
        "chapters": 10, 
        "name": "Esther"
    }, 
    {
        "osis": "Job", 
        "chapters": 42, 
        "name": "Job"
    }, 
    {
        "osis": "Ps", 
        "chapters": 150, 
        "name": "Psalms"
    }, 
    {
        "osis": "Prov", 
        "chapters": 31, 
        "name": "Proverbs"
    }, 
    {
        "osis": "Eccl", 
        "chapters": 12, 
        "name": "Ecclesiastes"
    }, 
    {
        "osis": "Song", 
        "chapters": 8, 
        "name": "Song of Solomon"
    }, 
    {
        "osis": "Isa", 
        "chapters": 66, 
        "name": "Isaiah"
    }, 
    {
        "osis": "Jer", 
        "chapters": 52, 
        "name": "Jeremiah"
    }, 
    {
        "osis": "Lam", 
        "chapters": 5, 
        "name": "Lamentations"
    }, 
    {
        "osis": "Ezek", 
        "chapters": 48, 
        "name": "Ezekiel"
    }, 
    {
        "osis": "Dan", 
        "chapters": 12, 
        "name": "Daniel"
    }, 
    {
        "osis": "Hos", 
        "chapters": 14, 
        "name": "Hosea"
    }, 
    {
        "osis": "Joel", 
        "chapters": 3, 
        "name": "Joel"
    }, 
    {
        "osis": "Amos", 
        "chapters": 9, 
        "name": "Amos"
    }, 
    {
        "osis": "Obad", 
        "chapters": 1, 
        "name": "Obadiah"
    }, 
    {
        "osis": "Jonah", 
        "chapters": 4, 
        "name": "Jonah"
    }, 
    {
        "osis": "Mic", 
        "chapters": 7, 
        "name": "Micah"
    }, 
    {
        "osis": "Nah", 
        "chapters": 3, 
        "name": "Nahum"
    }, 
    {
        "osis": "Hab", 
        "chapters": 3, 
        "name": "Habakkuk"
    }, 
    {
        "osis": "Zeph", 
        "chapters": 3, 
        "name": "Zephaniah"
    }, 
    {
        "osis": "Hag", 
        "chapters": 2, 
        "name": "Haggai"
    }, 
    {
        "osis": "Zech", 
        "chapters": 14, 
        "name": "Zechariah"
    }, 
    {
        "osis": "Mal", 
        "chapters": 4, 
        "name": "Malachi"
    }, 
    {
        "osis": "Matt", 
        "chapters": 28, 
        "name": "Matthew"
    }, 
    {
        "osis": "Mark", 
        "chapters": 16, 
        "name": "Mark"
    }, 
    {
        "osis": "Luke", 
        "chapters": 24, 
        "name": "Luke"
    }, 
    {
        "osis": "John", 
        "chapters": 21, 
        "name": "John"
    }, 
    {
        "osis": "Acts", 
        "chapters": 28, 
        "name": "Acts"
    }, 
    {
        "osis": "Rom", 
        "chapters": 16, 
        "name": "Romans"
    }, 
    {
        "osis": "1Cor", 
        "chapters": 16, 
        "name": "1 Corinthians"
    }, 
    {
        "osis": "2Cor", 
        "chapters": 13, 
        "name": "2 Corinthians"
    }, 
    {
        "osis": "Gal", 
        "chapters": 6, 
        "name": "Galatians"
    }, 
    {
        "osis": "Eph", 
        "chapters": 6, 
        "name": "Ephesians"
    }, 
    {
        "osis": "Phil", 
        "chapters": 4, 
        "name": "Philippians"
    }, 
    {
        "osis": "Col", 
        "chapters": 4, 
        "name": "Colossians"
    }, 
    {
        "osis": "1Thess", 
        "chapters": 5, 
        "name": "1 Thessalonians"
    }, 
    {
        "osis": "2Thess", 
        "chapters": 3, 
        "name": "2 Thessalonians"
    }, 
    {
        "osis": "1Tim", 
        "chapters": 6, 
        "name": "1 Timothy"
    }, 
    {
        "osis": "2Tim", 
        "chapters": 4, 
        "name": "2 Timothy"
    }, 
    {
        "osis": "Titus", 
        "chapters": 3, 
        "name": "Titus"
    }, 
    {
        "osis": "Phlm", 
        "chapters": 1, 
        "name": "Philemon"
    }, 
    {
        "osis": "Heb", 
        "chapters": 13, 
        "name": "Hebrews"
    }, 
    {
        "osis": "Jas", 
        "chapters": 5, 
        "name": "James"
    }, 
    {
        "osis": "1Pet", 
        "chapters": 5, 
        "name": "1 Peter"
    }, 
    {
        "osis": "2Pet", 
        "chapters": 3, 
        "name": "2 Peter"
    }, 
    {
        "osis": "1John", 
        "chapters": 5, 
        "name": "1 John"
    }, 
    {
        "osis": "2John", 
        "chapters": 1, 
        "name": "2 John"
    }, 
    {
        "osis": "3John", 
        "chapters": 1, 
        "name": "3 John"
    }, 
    {
        "osis": "Jude", 
        "chapters": 1, 
        "name": "Jude"
    }, 
    {
        "osis": "Rev", 
        "chapters": 22, 
        "name": "Revelation"
    }
]);
//
//console.info(ESVBible)
//console.info(ESVBible.at(0).getChapter(1))
//