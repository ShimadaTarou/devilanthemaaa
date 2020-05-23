def shimada():
    print("あなたにオススメするデビアン楽曲")
    favorite_music=int(input("あなたの好きな曲のジャンルは？半角数字で答えてください。1.ポップス　2.ロック"))
    favorite_member=int(input("あなたの好きな女性のタイプは？半角数字で答えてください。1.モデル　2.赤ちゃん顔"))
    if favorite_music==1 and favorite_member==1:
        print("あなたにオススメするデビアンの曲は女の子警察です")
    elif favorite_music==1 and favorite_member==2:
        print("あなたにオススメするデビアンの曲はココロカラです")
    elif favorite_music==2 and favorite_member==1:
        print("あなたにオススメするデビアンの曲はfakefactorです")
    elif favorite_music==2 and favorite_member==2:
        print("あなたにオススメするデビアンの曲はEmotionnalです")
shimada()
