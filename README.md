# pdf_Interleave
pdf 두 파일을 교차하여 페이지 정렬

py 3.11.4

[venv]
py -3.11 -m venv venv
venv\Scripts\activate.bat

pip freeze > requirements.txt
pip install -r requirements.txt
pip uninstall -r requirements.txt -y
pip download -r requirements.txt


[git]
계정 변경 시
1. 이미 있는 정보를 삭제
git config --unset user.name
git config --unset user.email
만약 global로 했다면,
git config --unset --global user.name
git config --unset --global user.email

2. 삭제 확인
git config --list

3. 재설정
git config user.name "nickname"
git config user.email "helloWorld@gmail.com"
만약 global로 하려면,
git config --global user.name "nickname"
git config --global user.email "helloWorld@gmail.com"


[exe]
(최종) pyinstaller -w --onefile pdf교차편집.py
(console: 디버깅용) pyinstaller --onefile --console pdf교차편집.py