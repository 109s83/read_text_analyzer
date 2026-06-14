from text_analyzer.core import Document


class Tweet(Document):
    """트윗(Tweet)을 나타내는 클래스이며, text_analyzer의 부모 클래스로부터 Document를 상속받는다.

    :param text: 트윗 텍스트
    """

    def __init__(self, text): 
        super().__init__(text)  # 부모(Document)의 __init__ 그대로 사용

    def hashtag_count(self):
        """트윗에 포함된 해시태그(#) 개수 나타내기

        :return: 해시태그 개수

        예시

        >>> Tweet("I love #python and #coding").hashtag_count()
        2

        설명:트윗의 토큰리스트를 보면서 해시태그가 붙은 단어를 인식해 개수를 세어준다.
        반환된 값은 2

        """
        count = 0 # 0부터 시작
        for word in self.tokens: # 토큰에 있는 단어를 보면서
            if word.startswith('#'): #만약 word가 #으로 시작한다면
                count += 1 # count에 1을 더해준다
        return count # 그렇게해서 나온 값
    
    def mention_count(self):
        """트윗에 포함된 멘션(@) 개수를 반환합니다.

        :return: 멘션 개수

        예시

        >>> Tweet("Hi @alice and @bob, how are you?").mention_count()
        2

        설명:트윗의 토큰리스트를 보면서 멘션이 붙은 단어를 인식해 개수를 세어준다.
        반환된 값은 2

        """
        return sum(1 for word in self.tokens if word.startswith('@'))