# 차량 동역학 60일 코스 — NotebookLM 오디오 가이드

> 르노코리아 서스펜션 엔지니어를 위한 차량 동역학 자습 코스
> 총 60강, 약 7시간 분량의 오디오 강의 대본

## 사용 방법

### Google NotebookLM (추천)
1. [NotebookLM](https://notebooklm.google.com) 접속
2. 새 노트북 생성
3. Week별 .md 파일을 소스로 업로드 (한번에 1-2개씩)
4. '오디오 개요' 탭에서 AI 팟캐스트 생성 클릭
5. 생성된 오디오를 다운로드하여 차에서 재생

### Mac TTS
1. 시스템 설정 > 손쉬운 사용 > 음성 콘텐츠
2. 한국어 음성(Yuna) 다운로드
3. 텍스트 선택 후 Option+Esc으로 읽기

### OpenAI TTS API
```python
from openai import OpenAI
client = OpenAI()
response = client.audio.speech.create(
    model="tts-1-hd", voice="nova",
    input=open("Week01_Week_1.md").read()
)
response.stream_to_file("week01.mp3")
```

## 주차별 파일 목록

| Week 01 | Week 1: 진동 기초 I | ~44분 |
| Week 02 | Week 2: 공진·쿼터카·하프카 | ~38분 |
| Week 03 | Week 3: 전달함수·승차감 | ~34분 |
| Week 04 | Week 4: 서스펜션 부품 | ~30분 |
| Week 05 | Week 5: 트레이드오프·주파수 | ~30분 |
| Week 06 | Week 6: 모드해석·Simpack | ~36분 |
| Week 07 | Week 7: 디지털트윈·기구학 | ~31분 |
| Week 08 | Week 8: 서스펜션 기구학 | ~31분 |
| Week 09 | Week 9: 스티어링·코너링 | ~40분 |
| Week 10 | Week 10: 요응답·브레이크 | ~41분 |
| Week 11 | Week 11: 회생제동·고급주제 | ~37분 |
| Week 12 | Week 12: 능동서스펜션·완성 | ~34분 |

**전체 합계: 약 428분 (7.1시간)**