# from jose import jwt
# import requests
# from fastapi import HTTPException
# from app.core.config import AWS_REGION, USER_POOL_ID, CLIENT_ID

# def verify_token(token: str):
#     try:
#         jwks_url = f"https://cognito-idp.{AWS_REGION}.amazonaws.com/{USER_POOL_ID}/.well-known/jwks.json"
#         jwks = requests.get(jwks_url).json()

#         headers = jwt.get_unverified_header(token)

#         key = next(k for k in jwks["keys"] if k["kid"] == headers["kid"])

#         payload = jwt.decode(
#             token,
#             key,
#             algorithms=["RS256"],
#             audience=CLIENT_ID,
#         )

#         if payload.get("token_use") != "id":
#             raise HTTPException(status_code=401, detail="Invalid token")

#         return payload

#     except Exception:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")