from commitizen.cz.base import BaseCommitizen


class CzRu(BaseCommitizen):
    def questions(self) -> list:
        raise NotImplementedError("Not Implemented yet")

    def message(self, answers: dict) -> str:
        raise NotImplementedError("Not Implemented yet")
