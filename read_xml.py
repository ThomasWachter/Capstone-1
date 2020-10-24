from xml.etree import ElementTree as ET

doctree = ET.parse("tester.xml")
root = doctree.getroot()
print(root[0][0][0][1].text)

#https://www.youtube.com/watch?v=r6dyk68gymk
