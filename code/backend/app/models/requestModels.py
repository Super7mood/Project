from pydantic import BaseModel


class LLMRequest(BaseModel):
    prompt: str
    #type: str #To do, add this when react successfully connect with fast api
