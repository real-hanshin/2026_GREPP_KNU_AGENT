from langchain_core.tools import tool
from pydantic import BaseModel, Field
from mock_db import get_store

class ContactInfo(BaseModel):
    name: str = Field(description="수신자 이름")
    role: str = Field(description="직책")
    email: str = Field(description="이메일 주소")

class EmailDraft(BaseModel):
    subject: str = Field(description="이메일 제목")
    body: str = Field(description="이메일 본문")
    recipient_email: str = Field(description="수신자 이메일 주소")

@tool
def get_contact(name: str) -> str:
    """주소록에서 수신자의 직책과 이메일 주소를 조회합니다.

    Args:
        name: 검색할 수신자의 이름
    """
    store = get_store()
    contact = store["contacts"].get(name)
    if contact:
        return f"직책: {contact.role}, 이메일: {contact.email}"
    return f"'{name}'님의 정보를 찾을 수 없습니다."

@tool
def save_contact(name: str, role: str, email: str) -> ContactInfo:
    """새로운 수신자 정보를 주소록에 저장합니다.

    Args:
        name: 수신자의 이름
        role: 수신자의 직책
        email: 수신자의 이메일 주소
    """
    store = get_store()
    new_contact = ContactInfo(name=name, role=role, email=email)
    store["contacts"][name] = new_contact
    return new_contact

@tool
def save_email_draft(subject: str, body: str, recipient_email: str) -> str:
    """작성된 이메일 초안을 보관함에 저장합니다.

    Args:
        subject: 이메일 제목
        body: 이메일 본문 내용
        recipient_email: 수신자 이메일 주소
    """
    store = get_store()
    draft = EmailDraft(subject=subject, body=body, recipient_email=recipient_email)
    store["drafts"].append(draft)
    return "이메일 초안이 저장되었습니다."

@tool
def get_saved_drafts() -> str:
    """보관함에 저장된 이메일 초안 목록을 조회합니다."""
    store = get_store()
    drafts = store["drafts"]
    if not drafts:
        return "저장된 초안이 없습니다."
    
    return "\n".join([f"[{i+1}] {d.recipient_email} | {d.subject}" for i, d in enumerate(drafts)])