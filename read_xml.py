import os
from xml.etree import ElementTree
# https://www.youtube.com/watch?v=rFxXDO8-keg
filename = "XML_1601405161561.xml"
filepath = os.path.abspath(os.path.join('data', filename))
print(filepath)

dom = ElementTree.parse(filepath)
print(dom)

folio = dom.findall('Documento/Encabezado/IdDoc/Folio')
print(folio)
