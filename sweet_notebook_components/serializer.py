import json
from typing import Dict, Any
from sweet_notebook_components.component import Component


class Serializer:
    def serialize_to_json(self, component: Component) -> str:
        return json.dumps(self.__serialize_component(component), indent=2)

    def __serialize_component(self, component: Component) -> Dict[str, Any]:
        serialized_children = [
            self.serialize_component(child) for child in component.children
        ]

        return {
            "children": serialized_children,
            "props": component.internal_get_props_to_serialize(),
            "type": component.type,
        }
