"""
This script clean text related to POIs on roads, buildings, etc. from OSM maps.
The text was imported by OCAD.

Test on OSM format january 2020.
@author: isaaclera
"""
import xml.etree.cElementTree as ET

tagsToRemove = ['name','network','operator','addr:street','note','website',"ref"]
termsOn = ["relation","node","way"]: 

filename="map.osm"
fileout ="mapClean.osm"

tree = ET.parse(filename)
root = tree.getroot()
for term in termsOn: 
    relations=root.findall(term)
    for rel in relations:
       for tag in rel.getiterator():
           if tag.get('k') in tagsToRemove:
                  print ("- ",tag.get("v"))
                  tag.set('v',"")

tree.write(fileOut)
