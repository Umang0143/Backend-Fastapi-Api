import jwt
import requests
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.config import *

security = HTTPBearer()

# -------------------- JWKS --------------------
# Construct the JWKS URL based on the Cognito region and user pool ID. This URL is used to retrieve the JSON Web Key Set (JWKS) for verifying JWT tokens issued by AWS Cognito.
JWKS_URL = f"https://cognito-idp.{AWS_REGION}.amazonaws.com/{USER_POOL_ID}/.well-known/jwks.json"

def get_jwks():
    return requests.get(JWKS_URL).json()

# -------------------- TOKEN VERIFY --------------------
# This function verifies the JWT token sent in the Authorization header. It retrieves the JWKS from AWS Cognito, extracts the appropriate public key, and decodes the token to validate it and extract the payload.
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        jwks = get_jwks()

        headers = jwt.get_unverified_header(token)
        kid = headers["kid"]

        key = next(k for k in jwks["keys"] if k["kid"] == kid)
        public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)

        payload = jwt.decode(
            token,
            public_key,
            algorithms=["RS256"],
            audience=CLIENT_ID,
            leeway=30
        )

        return payload

    except Exception as e:
        print("JWT ERROR:", str(e))
        raise HTTPException(status_code=401, detail=str(e))