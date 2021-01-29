import requests

API_ENDPOINT = "https://api.pgamerx.com"
JOKE_ENDPOINT = API_ENDPOINT + "/joke"
IMAGE_ENDPOINT = API_ENDPOINT + "/image"
AI_ENDPOINT = API_ENDPOINT + "/ai"


class RandomStuff:


    """
    A Wrapper for the Random Stuff API.

    Example Usage:
    
        rs = RandomStuff()
        rs.create_session()
        joke = rs.get_joke()
        print(joke)
    """
    def __init__(self):
        self.session = None

    def create_session(self):
        self.session = requests.Session()

    def get_joke(self,_type="any"):

        jokeEndpoint = JOKE_ENDPOINT+ f"/{_type}"
        with self.session.get(jokeEndpoint) as response:
            result = response.json()
        return result

    def get_image(self,_type="any"):

        imgEndpoint = IMAGE_ENDPOINT+ f"/{_type}"
        with self.session.get(imgEndpoint) as response:
            result = response.json()
        return result

    def get_ai_response(self,msg):

        aiEndpoint = AI_ENDPOINT+ f"/response?message={msg}&?lanuage=en"
        with self.session.get(aiEndpoint) as response:
            result = response.json()
        return result


    def close(self):
        return self.session.close()

