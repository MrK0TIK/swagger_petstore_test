import requests


class ApiFunctions:
    Session = requests.session()

    @classmethod
    def post_function(cls, url, data):
        post = cls.Session.post(url, data)
        print("-----request begins-----\n")
        print(post.request.body)
        print("\n-----request ends-----\n")
        print("-----response begins-----\n")
        print(post.text)
        print("\n-----response ends-----\n")
        return post

    @classmethod
    def get_function(cls, url, data):
        get = cls.Session.get(url, data)
        print("-----request begins-----\n")
        print(get.request.body)
        print("\n-----request ends-----\n")
        print("-----response begins-----\n")
        print(get.text)
        print("\n-----response ends-----\n")
        return get

