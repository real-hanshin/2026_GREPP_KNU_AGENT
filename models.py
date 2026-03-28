"""
대학생 이메일 초안 작성 에이전트 데이터 모델
"""

from pydantic import BaseModel, Field
from typing import Optional

class EmailInfo(BaseModel):
    sender_name: str = Field(description="사용자의 이름")
    sender_student_id: str = Field(description="사용자의 학번")
    sender_department: str = Field(description="사용자의 소속 학과")
    
    recipient_name: str = Field(description="수신자의 이름")
    recipient_role: str = Field(description="수신자의 직책 (예: 교수님, 조교님, 선배님)")
    
    recipient_email: Optional[str] = Field(None, description="수신자의 이메일 주소")
    course_name: Optional[str] = Field(None, description="관련 과목명 (선택 사항)")
    course_section: Optional[str] = Field(None, description="분반 (선택 사항)")
    
    purpose: str = Field(description="이메일 전송 목적 (예: 성적 문의, 결석 출석 인정 요청, 프로젝트 팀원 모집)")
    tone: str = Field(description="이메일 어조(예: 정중하게, 친근하게)")

class EmailGuideLine(BaseModel):
    subject: str = Field(description="이메일 제목 (과목명과 분반, 이름, 목적이 포함된 직관적인 제목)")
    body: str = Field(description="이메일 본문 (인사말, 소속/신분 밝히기, 본론, 맺음말 포함)")

