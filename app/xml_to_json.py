import xml.etree.ElementTree as ET
def xml_to_json(xml_bytes: bytes):
    root = ET.fromstring(xml_bytes)
    items = root.findall(".//item")
    result = []

    for item in items:
        item_dict = {}
        for child in item:
            item_dict[child.tag] = child.text
        result.append(item_dict)
    
    return result