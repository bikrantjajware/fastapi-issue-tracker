from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List

class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=3, max_length=100)
    priority: IssuePriority = IssuePriority.medium
    status: IssueStatus = IssueStatus.open

class IssueUpdate(BaseModel):
    title : Optional[str] = Field(default=None, min_length=3, max_length=30)
    description : Optional[str] = Field(default=None, min_length=3, max_length=100)
    priority : Optional[IssuePriority] = None
    status : Optional[IssueStatus] = None


class IssueOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: Optional[IssueStatus] 
    priority: Optional[IssuePriority] 

class IssueResponse(BaseModel):
    data: Optional[IssueOut]
    error: Optional[str] = None

class IssueListResponse(BaseModel):
    data: List[IssueOut]
    error: Optional[str] = None
