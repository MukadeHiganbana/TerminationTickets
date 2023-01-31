from jira import JIRA

from config import Config


class JiraManager:
    def __init__(self):
        self.config = Config()
        self.server = self.config["JIRA"]["server"]
        self.login = self.config["JIRA"]["login"]
        self.api_key = self.config["JIRA"]["api_key"]
        self.project = self.config["JIRA"]["project"]
        self.jira_options = {"server": self.server}
        self.jira = JIRA(options=self.jira_options, basic_auth=(self.login, self.api_key))
