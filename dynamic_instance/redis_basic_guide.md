
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
