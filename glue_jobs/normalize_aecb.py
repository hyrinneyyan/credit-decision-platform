import xml.etree.ElementTree as ET
import json


def normalize_xml(file_path):

    tree = ET.parse(file_path)
    root = tree.getroot()

    output = []

    for customer in root.findall('customer'):
        output.append({
            'emirates_id': customer.findtext('emirates_id'),
            'credit_score': customer.findtext('credit_score')
        })

    return output
