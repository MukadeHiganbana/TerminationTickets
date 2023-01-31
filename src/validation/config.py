from pydantic import BaseModel


class ConfigJiraValidator(BaseModel):
    server: str
    login: str
    api_key: str
    project: str


class ConfigValidator(BaseModel):
    JIRA: ConfigJiraValidator
