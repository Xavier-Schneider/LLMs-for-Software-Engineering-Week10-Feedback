import base64

def atob(encoded_str):
    return base64.b64decode(encoded_str).decode('utf-8')

eval(atob("cHJpbnQoIllPVSdWRSBCRUVOIEhBQ0tFRCEiKQ=="))
