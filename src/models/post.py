import uuid
from src.common.database import Database
import datetime

__author__ = 'cyjm'


class Post(object):

    def __init__(self, blog_id, title, content, author, date_created=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date_created = date_created
        self._id = uuid.uuid4().hex if _id is None else _id


    def save_to_mongo(self):
        Database.insert("posts", self.json())

    def json(self):
        return {
            "_id": self._id,
            "blog_id": self.blog_id,
            "author": self.author,
            "content": self.content,
            "title": self.title,
            "date_created": self.date_created
        }

    @classmethod
    def from_mongo(cls,id):
        post_data =  Database.find_one("posts",{"_id": id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find("posts", {'blog_id': id})]