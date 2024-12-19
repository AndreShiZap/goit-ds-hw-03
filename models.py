from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE

connect(db="hw", host="mongodb+srv://andreshizap:567234@cluster0.pqxcf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#mongodb://localhost:27017


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=50))
    quote = StringField()
    meta = {"collection": "quotes"}

    def to_json(self, *args, **kwargs):
        data = self.to_mongo(*args, **kwargs)
        data["author"] = self.author.fullname