from dataclasses import dataclass

@dataclass
class Retailer:
    code: int
    name: str

    def __hash__(self):
        return self.code

    def __str__(self):
        return self.name