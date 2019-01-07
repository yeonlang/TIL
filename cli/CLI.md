# CLI
- CLI : Command Line Interface # 명령어 줄 인터페이스
- GUI : Graphic User Interface # 그래픽으로 구성된 사용자 조직 인터페이스
- prom : $ 앞의 내용을 프롬프트라고 한다. 내용은 수정 가능 
- shell : 컴퓨터와 상호작용할 수 있도록 명령어를 입력하여 사용하는 인터페이스 프로그램
- echo : 텍스트라인을 보여주는 명령어 : 그대로 출력  : SHELL을 출력
- man 명령어 : 명령어의 설명을 보여주는 명령어

## Exercises
1. `터미널에 Hello world` 라고 입력하고 이 문제상황에서 빠져나와 보자'
2. `echo 'hello`라고 입력하고 이 문제상황에서 빠져나와 보자.
3. `echo` 매뉴얼을 참고하여 줄 바꿈(개행, newline)을 하지 않고 'hello, world'를 출력해 보자 (echo -n 'hello, world') 
4. `sleep`이라고 하는 명령어의 매뉴얼 페이지를 읽고 , 우리의 터미널을 5초간 재워보자(sleep 5)
5. 이번에는 터미널을 100초간 재워보고 , 중간에 깨워보도록 하자.(^c)

## Summary
- `echo <string>` : 화면에 문자열 출력. ex) echo hello
- `man <command>` : 특정 커맨드 매뉴얼 페이지. ex) man echo
- `^c` : 현재 입력중인 작업 취소(Cancel) 이후 새 줄 실행.
- `^a` : 현재 입력중이 줄 맨 앞으로 커서 이동.
- `^e` : 현재 입력중이 줄 맨 뒤로 커서 이동
- `^u` : 현재 커서 기준, 앞쪽 전체 삭제.
- `^k` : 현재 커서 기준, 뒷쪽 전체 삭제.
- `^w` : 현재 커서 기준, 앞쪽 단어 단위로 삭제. (c9에서는 사용 불가)
- `alt + click` : 클릭하는 곳으로 커서 이동.
- `방향키 위, 아래` : 명령어 히스토리 탐색
- `clear` or `^l` : 화면 정리(clear screen)
- `exit` or `^d` : bash 종료