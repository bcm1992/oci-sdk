# %% Initialize
import oci
import base64
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
secret_client = oci.secrets.SecretsClient(config={}, signer=signer)

# %% display a secret

secret_id = 'ocid1.vaultsecret.oc1.phx.amaaaaaahlageniawrrsz5dooljt5tkly225mdafwgfue2ssutyp254fuuqa'
print(base64.b64decode(secret_client.get_secret_bundle(secret_id=secret_id).data.secret_bundle_content.content).decode('utf-8'))
