import httpx
from apiclient import APIClient, APIRouter, Get, endpoint


class RandomStuff(APIClient):
    """
    A Wrapper for the Random Stuff API.

    Example Usage:

        rs = RandomStuff(api_key = "Your API Key")
        joke = rs.get_joke()
        print(joke)
        rs.close()

    Example async usage:
        rs = RandomStuff(async_mode=True, api_key="Your API Key")
        joke = await rs.get_joke()
        print(joke)
        await rs.close()
    """

    _joke_types = ("dev", "spooky", "pun", "any")
    _image_types = (
        "aww",
        "duck",
        "dog",
        "cat",
        "memes",
        "dankmemes",
        "holup",
        "art",
        "harrypottermemes",
        "facepalm",
        "any",
    )

    def __init__(self, *, async_mode=False, api_key: str = None):
        session = httpx.AsyncClient() if async_mode else httpx.Client()
        self.base_url = "https://api.pgamerx.com"
        if api_key:
            session.params["api_key"] = api_key
        else:
            self.base_url += "/demo"
            
        self.api_key = api_key
        super().__init__(session=session)

    def _pre_init(self):
        # Convert to json before returning
        self._post_processors.append(lambda res: res.json())

    @endpoint
    def get_joke(self, _type: str = "any") -> dict:
        """Gets a random joke
        
        Parameters:
            - _type (str): The type of joke. Leave it or use `any` for a random type.
                           Can be: ('dev', 'spooky', 'pun', 'any')
        
        Returns:
            - str: The random joke
        """
        
        _type = _type.lower()
        if _type.lower() not in self._joke_types:
            raise RuntimeError("Unknown joke type provided: {}".format(_type))

        return Get("/joke/" + _type)

    @endpoint
    def get_image(self, _type: str = "any") -> str:
        """Gets a random image
        
        Parameters:
            - _type (str): The type of joke. Use `any` for a random type.
                           Can be: ('aww', 'duck', 'dog', 'cat', 'memes', 'dankmemes', 'holup', 'art', 'harrypottermemes', 'facepalm', 'any')
        
        Returns:
            - str: The random joke
        """
        _type = _type.lower()
        if _type not in self._image_types:
            raise RuntimeError("Unknown image type provided: {}".format(_type))

        return Get("/image/" + _type)

    @endpoint
    def get_ai_response(self, msg: str, *, lang="en") -> str:
        """Gets random AI response
        
        Parameters:
            - msg (str): The message on which the response is required.
            - lang (str): The language in which response is required. It is `en` (English) by default.
        
        Returns:
            - str : The random response.
        """
        return Get("/ai/response", params={"message": msg, "language": lang})

    def _post_get_image(self, res):
        return res[0]

    _post_get_ai_response = _post_get_image

    def close(self):
        """Closes a sync httpx client. For async usage, Use `RandomStuff.aclose()` method instead"""
        return self.session.close()

    async def aclose(self):
        """Closes an Async httpx client. For normal usage, Use `RandomStuff.close()` method instead"""
        return await self.session.aclose()

