- 출처 : [https://www.acmicpc.net/problem/1092](https://www.acmicpc.net/problem/1092)

- 풀이
    1. 크레인 리스트, 박스 리스트 내림차순 정렬
    2. 모든 크레인에 대해 이동 가능한 무게의 박스 각각 저장
    3. 모든 크레인을 돌면서 이동 가능한 무게의 박스 중아직 이동하지 않은 박스 이동
    4. 3번을 모두 이동할 때까지 반복

- 소감
    - 혼자 시도했던 풀이가 시간 초과가 나서 검색해서 나온 풀이를 참고했다
    - 정답 풀이와 다른 점은
        - 나는 이동이 안 된 박스를 찾을 때 전체 박스에 대해 탐색을 했고
        - 정답은 가능한 무게의 박스만 탐색을 해서 그런 것 같다