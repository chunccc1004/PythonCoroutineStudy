# PythonCoroutineStudy
## Coroutine basic info
- version : 3.8+
---
## Study env
- version : 3.11
- references :
  - https://docs.python.org/ko/3.11/library/asyncio-task.html
---
# 개념 정리
## awaitables  
객체가 await 표현식에서 사용될 수 있을 때, awaitables 객체라고 칭함
주요 세가지 유형
- 코루틴
- 테스크
- 퓨처
### 코루틴
파이썬 코루틴은 어웨이터블이므로 다른 코루틴에서 기다릴 수 있음
- 코루틴 함수 : async def 함수
- 코루틴 객체 : 코루틴 함수를 호춣여 반환된 객체
### 테스크
태스크는 코루틴을 동시에 예약하는 데 사용됨  
코루틴이 asyncio.create_task()와 같은 함수를 사용하여 테스크로 싸일 때 코루틴은 곧 실행되도록 자동으로 예약됨