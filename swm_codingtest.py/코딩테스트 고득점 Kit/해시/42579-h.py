def solution(genres, plays):
    from collections import defaultdict
    
    # (1) 장르별 총 재생수
    total_plays = defaultdict(int)
    # (2) 장르별 곡 저장
    songs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        total_plays[g] += p
        songs[g].append((i, p))
    
    # (3) 장르 정렬
    genre_order = sorted(total_plays, key=lambda g: total_plays[g], reverse=True)
    
    answer = []
    for g in genre_order:
        # (4) 해당 장르 곡 정렬
        # 재생수 내림차순, 같으면 인덱스 오름차순
        songs[g].sort(key=lambda x: (-x[1], x[0]))
        
        # (5) 최대 2곡 선택
        for i, play in songs[g][:2]:
            answer.append(i)
    
    return answer
