# %% Initialize
import requests
import oci
import os
import base64
#from Crypto.PublicKey import RSA
#from hashlib import sha256

#config = oci.config.from_file(file_location="~/.oci/config")
#tenancy_ocid=config['tenancy']
#user_ocid=config['user']
#key_fingerprint=config['fingerprint']

# %%
compartment_id = 'ocid1.tenancy.oc1..aaaaaaaa4urekisn2lfbmmakjnglv636ncsb36v4kxgu2yoygpbhiz3bqdpq'
bucket_name = 'terraform-bcm1992-state'
object_name = 'terraform.tfstate'
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

# listing the buckets in the object storage account
object_storage_client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
print(object_storage_client.get_namespace().data)

#print(object_storage_client.list_buckets(namespace_name=object_storage_client.get_namespace().data, compartment_id=compartment_id).data)

same_obj = object_storage_client.get_object(object_storage_client.get_namespace().data, bucket_name, object_name)
print('Object that we get from the bucket: {}'.format(same_obj.data.content))