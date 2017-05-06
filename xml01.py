import xml.etree.cElementTree as ET

root = ET.Element("tracking_data")
root.set("tracking_data_site", "FDBID")
root.set("mpe_id", "WebATLAS-MachineID")
root.set("runstart", "datetime of scan")

#----------------------------------- 

#ET.SubElement(root, "grafgsdfdas").set("vsafd", "hdsgrdgfag")
ulti = ET.SubElement(root, "UnitLoadTransacationIdentifier")
ulti.set("Ums_id","1")
ulti.set("UlxVersion","ULX 1.2")
ulti.set("Op","Label Generation")
ulti.set("MachineName","WebATLAS IPAddresss")
ulti.set("MachineSoftwareVersion","3.1.00")
ulti.set("SerialNumber","IP ???")
ulti.set("Machine_id","12345")
ulti.set("EventNum","1")
ulti.set("MachState","Ready")
ulti.set("TimeStamp","654265265265265")

#-----------------------------------------
hul = ET.SubElement(root, "HandlingUnitLoad")
hul.set("HandlingUnit_id","24 digit barcode")
hul.set("HandlingUnitType","0")

#-----------------------------------
rte = ET.SubElement(root, "Routing")
rte.set("OperationNum","00000")
rte.set("SortPlan","Label File Name??")
rte.set("DestName","Destination name")
rte.set("CinText","CIN Text")
rte.set("CarrierRoute","ROUTE")
rte.set("RunNum","0")
rte.set("RunoutNum","01")

#-----------------------------------
pa = ET.SubElement(root, "ProcAction")
pa.set("Action","Label Generation WebATLAS")

#ET.SubElement(doc, "field1", name="blah").text = "some value1"
#ET.SubElement(doc, "field2", name="asdfasd")

tree = ET.ElementTree(root)
tree.write("C:\\TEMP\\xmlsamp.xml", xml_declaration=True, encoding='utf-8', method="xml")