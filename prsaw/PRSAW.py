from aiohttp import ClientSession
from urllib.parse import quote

class RandomStuff:
    """
    A Wrapper for the Random Stuff API.

    Example Usage:
    
        rs = RandomStuff()
        joke = await rs.get_joke()
        print(joke)
        await rs.close()
    """
    def __init__(self):
        self.session = ClientSession()
        self.base_url = "https://api.pgamerx.com"
        self._joke_types = ("dev", "spooky", "pun")
        self._image_types = ("aww", "duck", "dog", "cat", "memes", "dankmemes", "holup", "art", "harrypottermemes", "facepalm")

    async def get_joke(self, _type: str = "any") -> dict:
        if _type.lower() not in self._joke_types:
            _type = "any"
        
        response = await self.session.get(f"{self.base_url}/joke/{_type.lower()}")
        try:
            return await response.json()
        except:
            return

    async def get_image(self, _type: str = "any") -> str:
        if _type.lower() not in self._image_types:
            _type = "any"
        
        response = await self.session.get(f"{self.base_url}/image/{_type.lower()}")
        try:
            json = await response.json()
            return json[0]
        except:
            return

    async def get_ai_response(self, msg):
        response = await self.session.get(f"{self.base_url}/ai/response?message={quote(msg)}")
        try:
            json = await response.json()
            return json[0]
        except:
            return

    async def close(self):
        return await self.session.close()