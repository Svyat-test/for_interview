from typing import Text
import dataclasses


@dataclasses.dataclass
class User:
    login: Text = ""
    password: Text = ""
