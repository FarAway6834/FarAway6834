# CSS 디버깅 방법

1. 비적용여부 디버깅 : Element 탭 내 Styles 탭에서 코드의 취소선 여부
2. 최종 렌더링 결과 디버깅 : Element 탭 내 Computed 탭에서 결과적 스타일 명시 내용
3. 에러 중 경고 확인법 : Element 탭 내 Styles 탭에서 경고가 뜨면 마우스를 올려서 확인한다
4. 에러 중 확실한 CSS상 문제의 이슈 확인법 : DevTools의 Issues 패널에서 치명적인 CSS 파싱 오류나 웹 표준에 어긋난 문제들의 리포트를 확인.
5. 린터 이용 : VS Code의 Stylelint를 이용하는 방법 (린팅 한정 ㅈㄴ 확실)