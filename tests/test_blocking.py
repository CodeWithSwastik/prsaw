import pytest

from prsaw import RandomStuff

from . import joke_response_keys


class TestBlocking:
    def setup(self):
        self.rs = RandomStuff()

    def test_invalid_joke_error(self):
        with pytest.raises(RuntimeError) as exc:
            self.rs.get_joke("deva")
        assert "deva" in str(exc)

    def test_invalid_image_error(self):
        with pytest.raises(RuntimeError) as exc:
            self.rs.get_image("awww")
        assert "awww" in str(exc)

    def test_joke_response(self):
        response = self.rs.get_joke("dev")

        assert isinstance(response, dict)
        assert set(response.keys()).issuperset(joke_response_keys)

    def test_ai_response(self):
        response = self.rs.get_ai_response("Hello!")

        assert isinstance(response, str)

    def test_image_reponse(self):
        response = self.rs.get_image("aww")

        assert isinstance(response, str)

    def teardown(self):
        self.rs.close()
