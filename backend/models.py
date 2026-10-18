from sqlmodel import SQLModel, Field

class t_base(SQLModel):
    name: str
    info: str

class t(t_base, table = True):
    id: int = Field(default = None, primary_key = True)

class append_info(t_base):
    pass