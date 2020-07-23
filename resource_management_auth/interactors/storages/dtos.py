from dataclasses import dataclass
import datetime

@dataclass
class UserDetailsDTO:
    user_id: int
    is_admin: bool

@dataclass
class UserAuthTokensDTO:
    user_id: str
    expires_in: datetime.datetime
    access_token: str
    refresh_token: str
    is_admin: bool
