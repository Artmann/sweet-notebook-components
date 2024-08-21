from typing import List, Dict, Any


class Component:

    def __init__(self, type):
        self.type = type
        self.children: List[Component] = []

    def text(self, body: str, help: str = None):
        component = Text(body, help)

        self.children.append(component)

        return component

    def internal_get_props_to_serialize(self):
        raise NotImplementedError(
            "Subclasses must implement get_props_to_serialize method"
        )


class Root(Component):
    def __init__(self):
        super().__init__(type="root")

    def internal_get_props_to_serialize(self) -> Dict[str, Any]:
        return {}

    def __del__(self):
        print("Root component deleted")


class Text(Component):
    def __init__(self, body, help=None):
        super().__init__(type="text")

        self.body = body
        self.help = help

    def internal_get_props_to_serialize(self) -> Dict[str, Any]:
        return {"body": self.body, "help": self.help}
