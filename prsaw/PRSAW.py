from enum import Enum

import httpx
from apiclient import APIClient, Get, endpoint


class BaseClient(APIClient):
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

    def close(self):
        session = self.session
        return (
            session.close() if isinstance(session, httpx.Client) else session.aclose()
        )


class RandomStuff(BaseClient):
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

    def __init__(self, *, async_mode=False, api_key: str = None):
        session = httpx.AsyncClient() if async_mode else httpx.Client()
        self.base_url = "https://api.pgamerx.com"
        if api_key:
            session.params["api_key"] = api_key
        else:
            self.base_url += "/demo"

        self.api_key = api_key
        super().__init__(session=session)

    @endpoint
    def get_ai_response(self, msg: str, *, lang="en") -> str:
        return Get("/ai/response", params={"message": msg, "language": lang})

    def _post_get_image(self, res):
        return res[0]

    _post_get_ai_response = _post_get_image


class ApiPlan(Enum):
    PRO = "pro"
    ULTRA = "ultra"
    BIZ = "biz"
    MEGA = "mega"


class RandomStuffV3(BaseClient):
    def __init__(
        self,
        api_key: str,
        *,
        async_mode=False,
        plan: ApiPlan = None,
        dev_name: str = None,
        bot_name: str = None,
        ai_language: str = None,
    ):
        session = httpx.AsyncClient() if async_mode else httpx.Client()

        # URL construction
        self.base_url = "https://api.pgamerx.com/v3"
        if plan:
            self.base_url += "/" + plan.value

        # Authorization
        if api_key:
            session.headers["x-api-key"] = api_key

        self.dev_name = dev_name
        self.bot_name = bot_name
        self.ai_language = ai_language

        self.api_key = api_key
        super().__init__(session=session)

    @endpoint
    def get_ai_response(
        self,
        message: str,
        *,
        unique_id: str = None,
        dev_name: str = None,
        bot_name: str = None,
        language: str = None,
    ):
        params = {"message": message}
        if unique_id:
            params["unique_id"] = unique_id

        if dev_name or self.dev_name:
            params["dev_name"] = dev_name or self.dev_name

        if language or self.ai_language:
            params["language"] = dev_name or self.ai_language

        if bot_name or self.bot_name:
            params["bot_name"] = bot_name or self.bot_name

        return Get("/ai/response", params=params)
