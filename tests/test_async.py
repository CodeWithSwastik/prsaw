from asyncio import get_event_loop

from prsaw import RandomStuff

from . import joke_response_keys


class TestAsync:
    def setup(self):
        self.rs = RandomStuff(async_mode=True)
        self.loop = get_event_loop()
        self.run = self.loop.run_until_complete

    def test_joke_response(self):
        response = self.run(self.rs.get_joke("dev"))

        assert isinstance(response, dict)
        assert set(response.keys()).issuperset(joke_response_keys)

    def test_image_response(self):
        response = self.run(self.rs.get_image("aww"))

        assert isinstance(response, str)

    def test_ai_response(self):
        response = self.run(self.rs.get_ai_response("Hello!"))

        assert isinstance(response, str)
