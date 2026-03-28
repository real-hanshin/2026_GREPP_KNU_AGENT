from agents import get_email_drafter_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatGroq(
        model="openai/gpt-oss-20b", 
        temperature=0.7
    )
    
    email_agent = get_email_drafter_agent(model)

    while True:
        print("\n1. 작성 가이드 예시 실행")
        print("2. 사용자 직접 입력")
        print("3. 종료")
        
        choice = input("선택 (1/2/3): ").strip()
        
        if choice == '1':
            content = (
                "나는 인공지능학과 3학년 조한신이야. 학번은 202203214이고. "
                "홍길동 교수님께 LLM기초 과목(01분반) 기말고사 범위 중 langchain 부분에 대해 "
                "질문하는 면담 요청 메일을 정중하게 작성해줘. "
                "교수님 메일은 hongGD@kongju.ac.kr이고, DB에 저장해줘."
            )
            print(f"\n입력: {content}")
            
            result = email_agent.invoke({
                "messages": [{"role": "user", "content": content}]
            })
            
            print("\n[실행 결과]")
            print(result['messages'][-1].content)
            
        elif choice == '2':
            content = input("\n입력: ").strip()
            if not content:
                continue
                
            result = email_agent.invoke({
                "messages": [{"role": "user", "content": content}]
            })
            
            print("\n[실행 결과]")
            print(result['messages'][-1].content)
            
        elif choice == '3':
            break
            
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()