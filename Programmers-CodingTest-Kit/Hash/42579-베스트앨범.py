'''
왜 이렇게 풀 수밖에 없는지 논리적으로 이해해둬라

- 장르별로 묶기 → 해시
묶지 않으면 장르별 총합을 계산할 수 없다.

- 장르 기준으로 정렬 → 총합 비교
장르 순서를 결정하는 유일한 정보는 총 재생수.

- 장르 안에서 정렬 → 상위 2곡 선택
장르별 우선순위를 명확히 정하는 유일한 방법.
'''

from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)     # 장르별 총 재생 수
    genre_songs = defaultdict(list)    # 장르별 (재생 수, 인덱스) 목록

    # ===== 1) 데이터 누적 단계 =====
    # zip + enumerate 로 i : 인덱스, g : 장르, p : 재생수
    for i, (g, p) in enumerate(zip(genres, plays)):
        # 첫 반복: i=0, g="classic", p=500
        genre_total[g] += p
        # genre_total → {"classic": 500}

        genre_songs[g].append((p, i))
        # genre_songs → {"classic": [(500, 0)]}


        # 두 번째 반복: i=1, g="pop", p=600
        # genre_total → {"classic": 500, "pop": 600}
        # genre_songs → {"classic": [(500,0)], "pop": [(600,1)]}

        # 세 번째 반복: i=2, g="classic", p=150
        # genre_total → {"classic": 650, "pop": 600}
        # genre_songs → {"classic": [(500,0), (150,2)], "pop": [(600,1)]}

        # 네 번째 반복: i=3, g="classic", p=800
        # genre_total → {"classic": 1450, "pop": 600}
        # genre_songs → {"classic": [(500,0), (150,2), (800,3)], "pop": [(600,1)]}

        # 다섯 번째 반복: i=4, g="pop", p=2500
        # genre_total → {"classic": 1450, "pop": 3100}
        # genre_songs → {"classic": [(500,0), (150,2), (800,3)], "pop": [(600,1), (2500,4)]}


    # ===== 2) 장르별 총 재생수 기반 정렬 =====
    # genre_total.items()는 아래처럼 보임:
    #   [("classic", 1450), ("pop", 3100)]
    #
    # key=lambda x: -x[1] → 총 재생수 내림차순 정렬
    #
    # sorted 결과:
    #   [("pop", 3100), ("classic", 1450)]
    sorted_genres = sorted(genre_total.items(), key=lambda x: -x[1])


    answer = []

    # ===== 3) 각 장르별로 상위 2개 뽑기 =====
    for g, _ in sorted_genres:
        # g="pop"부터 시작 -> genre_songs["pop"]
        # genre_songs["pop"] = [(600,1), (2500,4)]

        # 정렬 기준: 재생수 내림차순(-p), 인덱스 오름차순(i)
        # 정렬 후:
        #   [(2500,4), (600,1)]
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))

        # 상위 첫 곡 → 인덱스 4
        answer.append(songs[0][1])   # answer = [4]

        # 두 번째 곡 존재 → 인덱스 1
        answer.append(songs[1][1])   # answer = [4, 1]


        # 다음 장르 g="classic"
        # genre_songs["classic"] = [(500,0), (150,2), (800,3)]
        # 정렬:
        #   [(800,3), (500,0), (150,2)]
        # 상위 2개 → 3, 0
        # answer = [4, 1, 3, 0]

    return answer
