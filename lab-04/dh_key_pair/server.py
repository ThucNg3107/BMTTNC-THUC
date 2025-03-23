from cryptography.hazmat.primitives.asymmetric import dh 
from cryptography.hazmat.primitives import serialization

def generate_dh_parameters():
    # Generate DH parameters
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters
def generate_dh_key_pair(parameters):
    # Generate DH key pair
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key
def main():
    parameters=generate_dh_parameters()
    private_key, public_key=generate_dh_key_pair(parameters)
    
    with open("server_public_key.pem","wb") as f:
        f.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo))
if __name__ == "__main__":
    main()
# The server generates DH parameters and a DH key pair, and saves the public key to a file.