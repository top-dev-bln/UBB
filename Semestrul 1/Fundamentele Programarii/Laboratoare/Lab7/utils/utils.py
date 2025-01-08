import hashlib
import base64

def generate_id(lab, prb):
    """
    Generez un cod unic pentru un laborator si o problema.

    Param:
    lab - intreg, numarul laboratorului
    prb - intreg, numarul problemei

    return:
    string, cod unic
    """
    combined = f"{lab}-{prb}"
    
    hash_object = hashlib.sha256(combined.encode())

    hex_dig = hash_object.hexdigest()
  
    base64_encoded = base64.urlsafe_b64encode(bytes.fromhex(hex_dig)).decode('utf-8')
    
    return base64_encoded


