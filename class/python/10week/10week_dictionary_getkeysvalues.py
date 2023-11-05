song = {"작은 것들을 위한 시":"방탄소년단", "하기나해":"GRAY"}
print("곡명과 가수를 저장해봅시다.")
title = input("곡명:")
singer = input("가수:")
song[title] = singer

#list화 한 것이다.
print("\n곡 목록:", list(song.keys()))
print("\n곡 목록:", list(song.values()))

print()
print(f"곡명:'작은것들을 위한 시', 가수{song.get('작은 것들을 위한 시')}")

      
