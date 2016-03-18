import json
import xml.etree.ElementTree as ET

class ClassName:
    @property
    def class_name(self):
        return self.__class__.__name__

class Jsonable(ClassName):
    def to_json(self, indent = 4):
        d = {
        "dict": self.__dict__,
        "class_name": self.class_name
        }
        return json.dumps(d)

    @classmethod
    def from_json(self, json_string):
        attributes = json.loads(json_string)

        if not isinstance(attributes, dict) or\
        attributes.pop('class_name') != self.__name__:
            raise ValueError
        return self(**attributes['dict'])


class Xmlable(ClassName):
    def to_xml(self):
        root = ET.Element(self.class_name)
        cls_dict = self.__dict__
        for k, v in cls_dict.items():
            x = ET.SubElement(root,k)
            x.text = str(v)
        return ET.tostring(root)

    @classmethod   
    def from_xml(self,xml_str):
        root = ET.fromstring(xml_str)
        d = {ch.tag: ch.text for ch in root.getchildren()}
        return self(**d)
        