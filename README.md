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
### 퓨처
Future는 비동기 연산의 최종 결과를 나타내는 특별한 저수준 어웨이터블 객체  
Future 객체를 기다릴 때, 그것은 코루틴이 Future가 다른 곳에서 해결될 때까지 기다릴 것을 뜻함  
콜백 기반 코드를 async/await와 함께 사용하려면 asyncio의 Future 객체가 필요함  
일반적으로 응용 프로그램 수준 코드에서 Future 객체를 만들 필요는 없음  
때때로 라이브러리와 일부 asyncio API에 의해 노출되는 Future 객체를 기다릴 수 있음  
```python
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```