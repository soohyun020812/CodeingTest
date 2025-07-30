
# Redis란? 🤔

Redis는 **Remote Dictionary Server**의 줄임말로, 메모리 기반의 **키-값 저장소(key-value store)** 입니다.
일반적으로 데이터베이스로 사용되기도 하고, **캐시**, **메시지 브로커**, **세션 저장소** 등 다양한 용도로 활용됩니다.

---

## 핵심 특징 ✨

- **In-Memory 저장소**: 모든 데이터를 RAM에 저장하여 매우 빠른 읽기/쓰기 속도를 제공합니다.
- **Key-Value 구조**: 데이터를 `key`와 `value` 쌍으로 저장합니다.
- **다양한 데이터 타입 지원**:
  - `String`
  - `List`
  - `Set`
  - `Hash`
  - `Sorted Set`
  - `Stream` 등
- **지속성(Persistence) 지원**:
  - `RDB`(스냅샷 방식)와 `AOF`(명령어 로그 방식)로 디스크에도 저장 가능
- **Pub/Sub**: 게시/구독 기반 메시지 전송 시스템으로도 사용 가능
- **단일 스레드 기반**: 하지만 워낙 빠르기 때문에 병렬성이 크게 문제되지 않음

---

## Redis는 언제 쓰일까? 🔧

| 용도            | 설명 |
|-----------------|------|
| 캐시            | 자주 조회되는 데이터를 빠르게 제공 |
| 세션 저장소     | 로그인 정보 등을 임시로 저장 |
| 순위표/랭킹 시스템 | 점수 기반 정렬을 위한 Sorted Set 활용 |
| 실시간 채팅/알림 | Pub/Sub 기능 활용 |
| 큐 시스템       | List 자료형을 사용한 작업 대기열 구현 |
| 머신러닝 모델 관리 | 인스턴스 상태 캐시나 작업 대기열 구현 등 |

---

## 예시 명령어 💡

```bash
# Redis 클라이언트 접속
redis-cli

# 데이터 저장 및 조회
SET name "Suyeon"
GET name

# 리스트 사용 예시
LPUSH tasks "task1"
LPUSH tasks "task2"
LRANGE tasks 0 -1

# 삭제
DEL name

# 서버 상태 확인
PING
```

---

## Redis를 FastAPI + Celery와 함께 쓴다면? 🧵

- **Celery의 브로커로 사용**: 비동기 작업 큐로 메시지를 주고받기 위해 Redis를 중간 브로커로 사용합니다.
- **작업 상태 확인**: Redis가 각 작업의 상태와 결과를 관리합니다.

```python
# celery.py 예시
celery = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)
```

---

## 마무리 🌱

Redis는 속도가 매우 빠르고 다양한 기능을 갖춘 **초경량 데이터베이스**입니다.  
단순한 캐시부터 분산 시스템의 메시지 브로커 역할까지 다양하게 활용될 수 있습니다.

처음에는 어렵게 느껴질 수 있지만, 직접 명령어를 입력해보며 하나씩 익혀나가면 금방 친숙해질 거예요! 💪

> Redis 공식문서: https://redis.io/

> 위 redis_basic_guide는 chatGPT를 통해 정리되었습니다.


=============================
    📌 다시 복습하기!
=============================


### ✅ 1. Redis는 "초고속 노트"다 — 아주 빠른 key-value 저장소
> 비유 : 딥러닝 라벨링 팀에서 ```누가 어떤 모델을 쓰는 중```인지, ```어떤 작업이 대기 중```인지, ```학습이 끝났는지``` 종이에 적어서 실시간으로 다 같이 보는 상황.

이때 종이 대신 Redis를 사용
```redis
SET model1_status "running"
GET model1_status
=> "running"
```
> Redis는 디스크 대신 메모리에 저장하므로 매우 빠르지만, 전원이 꺼지면 날아갈 수 있음 (그러나 실시간 데이터 공유용으로는 최고)

### ✅ 2. Redis는 "대기열"이다 — 비동기 작업 처리 (Celery 브로커)
> 비유 : 고객이 "모델 학습 요청"을 했을 때, 그걸 바로 처리하지 않고 대기열에 넣어두면 작업자가 하나씩 꺼내서 처리함.

  - 고객 요청: FastAPI /```train```
  - 대기열에 등록: Celery가 Redis에 요청 메시지를 넣음
  - 작업자(worker): 대기열에서 꺼내서 처리
  - 결과 저장: Redis에 작업 상태를 저장하거나 결과를 반환

```python
# 작업 요청 (요청 → Redis)
task = train_model_task.delay(project_id)

# 결과 확인 (Redis에서)
task_result = task.get()
```

### ✅ 3. Redis는 "실시간 공유 캘린더"다 — 여러 프로세스가 동시에 상태 확인

  - model_1의 상태가 running인지 idle인지 모든 프로세스가 Redis를 통해 확인 가능
  - 동시에 여러 사용자가 접속 중일 때 상태 충돌 없이 관리 가능

### 👣 Redis 개념을 쉽게 익히는 방법 3단계
| 단계 | 설명 | 자료 |
|------|------|------|
| 🔹 1단계 | **CLI로 Redis 직접 조작해 보기** | [`redis-cli`](https://redis.io/docs/interact/redis-cli/) 실습 예시 (온라인 CLI 있음) |
| 🔹 2단계 | **Python에서 Redis 사용해 보기** |  |
| 🔹 3단계 | **내 프로젝트 흐름에 Redis가 어디에 쓰이는지 그림으로 그려보기** |  |

### 🧪 실습 예시
```python
# redis_test.py
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 상태 저장
r.set('model1_status', 'running')

# 상태 확인
print("Model 1 Status:", r.get('model1_status'))

# 상태 업데이트
r.set('model1_status', 'completed')

# 삭제
r.delete('model1_status')
```
> ```python redis_test.py```로 실행해보기

### ✍️ Redis 이미지
```less
[ FastAPI ] ---> [ Celery Task 요청 ]
      |                  |
      ↓                  ↓
  사용자 요청       Redis가 대기열로 관리
                          ↓
                   [ Celery Worker ]
                          ↓
                   작업 처리 중 상태를 Redis에 저장
```
