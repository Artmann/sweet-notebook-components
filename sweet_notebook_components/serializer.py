import json

from sweet_notebook_components.component import Component


class Serializer:
    def serialize_component(self, component: Component) -> str:
        return json.dumps(
            {
                "type": component.type,
                "props": component.internal_get_props_to_serialize(),
            },
            indent=2,
        )
