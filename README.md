# text_analyzer

텍스트를 분석해서 단어 수, 해시태그, 멘션 개수를 알려주는 패키지
다른 파일 텍스트에서도 추출이 가능하다.

## 설치 방법

```bash
pip install .
```

## 빠른 시작

```python
from text_analyzer.subclass import Tweet

t = Tweet("hello my name is #soojeong and @alice")
print(t.word_count())       # 결과출력 7
print(t.hashtag_count())    # 결과출력 1
print(t.mention_count())    # 결과출력 1
```

혹은 텍스트 파일로 분석하기:

```bash
python analyze.py # python analyze.py 실행
                               # ↓
                  # "분석할 텍스트 파일명을 입력하세요: " 창이 뜨면
                               # ↓
                  # 사용자가 test1.txt 입력
                               # ↓
단어 수, 해시태그 수, 멘션 수 출력
```

## 주요 기능

- 단어 수 계산 (word_count)
- 자주 나오는 단어 찾기 (most_common_words)
- 해시태그 개수 세기 (hashtag_count)
- 멘션 개수 세기 (mention_count)
- 텍스트 파일 읽기 (load_text_from_file)

## 테스트 실행

```bash
python -m pytest -v
```

## 작성자

- 이름: 이수정
- 학번: 202620882
- 이메일: soojeong@kku.ac.kr