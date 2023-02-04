#!/usr/bin/python3

import xml.etree.ElementTree as ET

data = """<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
    <item name="breakfast">Idly</item>
    <price>$2.5</price>
    <description>
   Two idly's with chutney
   </description>
    <calories>553</calories>
</food>
<food>
    <item name="breakfast">Paper Dosa</item>
    <price>$2.7</price>
    <description>
    Plain paper dosa with chutney
    </description>
    <calories>700</calories>
</food>
</metadata>

"""




my_tree = ET.fromstring(data)
#print(my_tree[0].tag)

for x in my_tree.findall("food"):
    calories = x.find("calories").text
    prices = x.find("price").text
    item = x.find("item")
    name = item.get("name")
    
    print(calories, prices, name)


# Modify tree

for desc in my_tree.iter("description"):
    new_desc = str(desc.text) + " will be served."
    desc.text = str(new_desc)
    desc.set("updated", "yes")

data = ET.XML(data)
with open("output.xml", "w") as file_xml:
    file_xml.write(str(ET.tostring(data)))
