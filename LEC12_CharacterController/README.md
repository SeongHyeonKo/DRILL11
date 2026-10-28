# LEC12 캐릭터 컨트롤러

## 실행 방법

이 폴더에서 `python main.py`를 실행합니다. 수업용 Pico2D 실행 환경이 필요합니다. 상태 머신 라이브러리는 다음 명령으로 설치할 수 있습니다.

```powershell
pip install -r requirements.txt
```

## 조작 방법

- 왼쪽/오른쪽 방향키: 누른 방향으로 달립니다. 모든 방향키를 떼면 IDLE로 돌아옵니다.
- `a` 키 (IDLE 상태): 5초 동안 AUTO_RUN을 시작합니다.
- AUTO_RUN 중 방향키: 자동 런을 취소하고 일반 RUN 상태로 전환합니다.
- SPACE (SLEEP 상태): 잠에서 깨어나 IDLE로 돌아옵니다.
- ESC: 프로그램을 종료합니다.

## 상태 및 파일

`boy.py`는 `transitions.Machine`으로 IDLE, RUN, SLEEP, AUTO_RUN 상태를 관리합니다. `auto_run.py`의 `AutoRun` 클래스는 자동 이동 동작을 담당합니다. AUTO_RUN은 더 빠르게 이동하고 스프라이트를 1.6배 확대하며 화면 가장자리에서 방향을 바꿉니다. `Boy.is_invincible` 값으로 무적 상태를 확인할 수 있습니다.

- `main.py`: 게임 루프와 키보드 입력 처리
- `boy.py`: 소년 상태 머신과 애니메이션
- `auto_run.py`: 자동 런 이동, 시간 제한, 확대 표시
- `state_diagram.svg`: 상태 전이 다이어그램
- `requirements.txt`: Python 의존성
