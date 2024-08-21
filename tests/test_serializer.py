from sweet_notebook_components.component import Text
from sweet_notebook_components.serializer import Serializer


def test_serialize_text_component() -> dict:
    text_component = Text("Hello, World!")

    serializer = Serializer()

    json = serializer.serialize_component(text_component)

    assert (
        json
        == """{
  "type": "text",
  "props": {
    "body": "Hello, World!",
    "help": null
  }
}"""
    )
