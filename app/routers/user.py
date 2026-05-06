from fastapi import APIRouter



UserRouter = APIRouter()

@UserRouter.post("/create_account")
def CreateAccount():
    return("account is created")
