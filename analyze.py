from text_analyzer.subclass import Tweet
from text_analyzer.utils import load_text_from_file

# 1. 사용자에게 파일명 입력받기
filename = input("분석할 텍스트 파일명을 입력하세요: ")

# 2. 파일에서 텍스트 읽기
text = load_text_from_file(filename)

# 3. Tweet 객체 만들기
tweet = Tweet(text)

# 4. 결과 출력
print(f"단어 수: {tweet.word_count()}")
print(f"해시태그 수: {tweet.hashtag_count()}")
print(f"멘션 수: {tweet.mention_count()}")
print(f"자주 나온 단어 Top 5: {tweet.most_common_words(5)}")