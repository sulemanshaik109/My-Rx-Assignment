from datetime import datetime
from typing import List, Tuple

class ImmutableEmployee:
    __slots__ = ("_name", "_id", "_date_of_joining", "_addresses")

    def __init__(self, name: str, emp_id: str, date_of_joining: datetime, addresses: List[Tuple[str, str]]):
        self._name = name
        self._id = emp_id
        self._date_of_joining = date_of_joining.replace()
        self._addresses = [(address[0], address[1]) for address in addresses]

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def date_of_joining(self) -> datetime:
        return self._date_of_joining.replace()
    
    @property
    def addresses(self) -> List[Tuple[str, str]]:
        return list(self._addresses)
    
    def __repr__(self) -> str:
        return (
            f"ImmutableEmployee(name={self._name}, id={self._id}, "
            f"date_of_joining={self._date_of_joining}, addresses={self._addresses})"
        )