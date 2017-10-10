# Djago 환경 설정

1. 프로젝트 폴더 만들기 

`command_line`
```
take <파일명>
# 파일명을 생성하고 해당 폴더로 이동한다
```

2. git init - 개인저장소 만들기

```commandline
git init
```

3. vi .gitignore

```commandline
vi .gitignore
```
/폴더명/ 안에 있는 .gitignore을 복사해서 현재 폴더로 가져온다
```commandline
cp ../-폴더명-/-폴더명-/ .
```
4. 가상환경 

가상환경 설치
```commandline
pyenv virtualenv 3.6.2 fc-<가상환경 명>
```
가상환경 local 지정
```commandline
pyenv local fc-djgirls
```
.gitignore 생성 사이트 

https://www.gitignore.io/

5. Django 프로젝트 시작

```commandline
django-admin startproject <프로젝트명>
```

'현재 버전을 요청'하는 관용적인 표현
```commandline
pip freeze > requirements.txt
```
6. pychrm open 

   - pycarm 가상환경 interpreter 설정
```
/usr/local/var/pyenv/versions/3.6.2/bin/python
```
7. 소스 루트 폴더 지정 

 pycharm 프로젝트 폴더 구조에서 
   루트 폴더 지정후 우클릭 
   Mark Directory as 에서 
   Sourses root 지정한다ㅕ777777777777ㅛ 
   

8. 어플리케이션 만들기
`manage.py`
```commandline
python manage.py startapp <config>
```
9. Django에 애플리캐이션 적용

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'config',  # 애플리케이션 폴더명
]
```
10. Django 프로젝트 `models.py` 만들기

11. 데이터 베이스 테이블 만들기

```commandline
./manage.py makemigrations
```

```commandline
./manage.py migrate
```

