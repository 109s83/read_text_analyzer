def load_text_from_file(filepath):
    """텍스트 파일에서 내용을 읽어온다.

    :param filepath: 읽을 파일의 경로
    :return: 파일 내용 문자열
    :raises FileNotFoundError: 파일이 존재하지 않을 경우

    >>> # example.txt 파일에 "Hello World"가 저장되어 있다고 가정
    >>> # load_text_from_file("example.txt") # 파일을 읽기 모드('r')로 열기, 한글 깨짐 방지용 인코딩 지정
    >>> # 'Hello World'
    """
    with open(filepath, 'r', encoding='utf-8') as f: # 파일을 열고, 작업 끝나면 자동으로 닫아줌
        return f.read() # 파일 내용을 문자열 전체로 읽기