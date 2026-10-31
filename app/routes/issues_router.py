from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueUpdate, IssueOut, IssueResponse, IssueListResponse
from typing import List, Optional
from app.storage import load, save


router = APIRouter(prefix='/issues', tags=['issues'])


issues = load()
ISSUE_ID = max((issue['id'] for issue in issues))+1 if issues else 1

@router.get('/')
def get_issues() -> IssueListResponse:
    return IssueListResponse(data=issues)

@router.get('/{issue_id}')
def get_issue(issue_id: int) -> Optional[IssueOut]:
    issue_gen = ( issue for issue in issues if issue['id'] == issue_id )
    try:
        issue = next(issue_gen)
        return IssueResponse(data=issue)
    except StopIteration:
        raise HTTPException(status_code=404, detail=f'issue not found')

@router.post('', status_code=status.HTTP_201_CREATED)
def create_issue(issue_in: IssueCreate) -> IssueResponse:
    global ISSUE_ID
    issue = issue_in.model_dump()
    print(issue)
    issue['id'] = ISSUE_ID
    ISSUE_ID += 1
    issues.append(issue)
    return {'data': issue }


@router.delete('/{issue_id}')
def delete_issue(issue_id: int) -> IssueResponse:
    issue_index = next((index for index, issue in enumerate(issues) if issue['id'] == issue_id), None)
    if issue_index is None:
        raise HTTPException(status_code=404, detail=f'issue {issue_id} not found')
    if issue_index is not None:
        deleted_issue = issues.pop(issue_index)
        save(issues)
        return IssueResponse(data=deleted_issue)

@router.put('/{issue_id}')
def update_issue(issue_id: int, issue_update: IssueUpdate) -> IssueResponse:
    issue_index = next(( idx for idx, issue in enumerate(issues) if issue['id'] == issue_id), None)
    if issue_index is None:
        raise HTTPException(status_code=404, detail=f'issue {issue_id} not found')
    issue = issues[issue_index]
    for key, value in issue_update:
            if value is not None:
                issue[key] = value
    issues[issue_index] = issue
    save(issues)


    
