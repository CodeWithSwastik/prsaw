import httpx
from apiclient import APIClient, APIRouter, Get, endpoint


class RandomStuff(APIClient):
    """
    A Wrapper for the Random Stuff API.

    Example Usage:

        rs = RandomStuff()
        joke = rs.get_joke()
        print(joke)
        rs.close()

    Example async usage:
        rs = RandomStuff(async_mode=True)
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
        _type = _type.lower()
        if _type.lower() not in self._joke_types:
            raise RuntimeError("Unknown joke type provided: {}".format(_type))

        return Get("/joke/" + _type)

    @endpoint
    def get_image(self, _type: str = "any") -> str:
        _type = _type.lower()
        if _type not in self._image_types:
            raise RuntimeError("Unknown image type provided: {}".format(_type))

        return Get("/image/" + _type)

    @endpoint
    def get_ai_response(self, msg: str, *, lang="en") -> str:
        return Get("/ai/response", params={"message": msg, "language": lang})

    def _post_get_image(self, res):
        return res[0]

    _post_get_ai_response = _post_get_image

    def close(self):
        return self.session.close()
