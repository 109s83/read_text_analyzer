# 실행 결과 요약

## pycodestyle 결과
```
python -m pycodestyle text_analyzer/
# 아무것도 안 나옴
```

## pytest 결과
```
 python -m pytest -v
================================================ test session starts ================================================
platform win32 -- Python 3.14.3, pytest-9.1.0, pluggy-1.6.0 -- C:\Users\solos\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\text_analyzer
collected 11 items                                                                                                   

tests/test_core.py::test_word_count_normal PASSED                                                              [  9%]
tests/test_core.py::test_most_common_words_normal PASSED                                                       [ 18%]
tests/test_core.py::test_most_common_words_top3 PASSED                                                         [ 27%]
tests/test_core.py::test_tokenize_lowercase PASSED                                                             [ 36%]
tests/test_core.py::test_hashtag_count_normal PASSED                                                           [ 45%]
tests/test_core.py::test_mention_count_normal PASSED                                                           [ 54%]
tests/test_core.py::test_word_count_empty PASSED                                                               [ 63%]
tests/test_core.py::test_most_common_words_empty PASSED                                                        [ 72%]
tests/test_core.py::test_word_count_spaces PASSED                                                              [ 81%]
tests/test_core.py::test_hashtag_count_none PASSED                                                             [ 90%]
tests/test_core.py::test_mention_count_none PASSED                                                             [100%]

================================================ 11 passed in 0.03s =================================================

```

## pip install . 결과
```
 pip install .
Processing c:\text_analyzer
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: text_analyzer
  Building wheel for text_analyzer (pyproject.toml) ... done
  Created wheel for text_analyzer: filename=text_analyzer-1.0.0-py3-none-any.whl size=4063 sha256=c34ea0d926759b6e2799c8ccd5d2e0a1e5f8c9cef35893872f2ac2681694f69d
  Stored in directory: C:\Users\solos\AppData\Local\Temp\pip-ephem-wheel-cache-h976w_ce\wheels\f2\c7\3b\0ff3013d9ce20902cbc103ca648dd7ed123aca4c169570117a
Successfully built text_analyzer
Installing collected packages: text_analyzer
  Attempting uninstall: text_analyzer
    Found existing installation: text_analyzer 1.0.0
    Can't uninstall 'text_analyzer'. No files were found to uninstall.
Successfully installed text_analyzer-1.0.0

[notice] A new release of pip is available: 25.3 -> 26.1.2
[notice] To update, run: C:\Users\solos\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pip install --upgrade pip

```