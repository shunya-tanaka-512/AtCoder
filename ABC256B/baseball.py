class Baseball:
    FIRST = 0
    SECOND = 1
    THIRD = 2

    # コンストラクタ(selfはオブジェクト自身)
    def __init__(self, runners, score):
        self.runners = runners
        self.score = score

    # スタティックメソッド（引数にself不要）
    @staticmethod  # Baseballの外から呼べる
    def play_ball():
        return Baseball([False, False, False], 0)

    # インスタンスメソッド
    def single_hit(self):
        if self.runners[self.THIRD]:
            self.runners[self.THIRD] = False
            self.score += 1
        if self.runners[self.SECOND]:
            self.runners[self.SECOND] = False
            self.runners[self.THIRD] = True
        if self.runners[self.FIRST]:
            self.runners[self.FIRST] = False
            self.runners[self.SECOND] = True
        self.runners[self.FIRST] = True

    def two_base_hit(self):
        if self.runners[self.THIRD]:
            self.runners[self.THIRD] = False
            self.score += 1
        if self.runners[self.SECOND]:
            self.runners[self.SECOND] = False
            self.score += 1
        if self.runners[self.FIRST]:
            self.runners[self.FIRST] = False
            self.runners[self.THIRD] = True
        self.runners[self.SECOND] = True

    def three_base_hit(self):
        if self.runners[self.THIRD]:
            self.runners[self.THIRD] = False
            self.score += 1
        if self.runners[self.SECOND]:
            self.runners[self.SECOND] = False
            self.score += 1
        if self.runners[self.FIRST]:
            self.runners[self.FIRST] = False
            self.score += 1
        self.runners[self.THIRD] = True

    def homerun(self):
        if self.runners[self.THIRD]:
            self.runners[self.THIRD] = False
            self.score += 1
        if self.runners[self.SECOND]:
            self.runners[self.SECOND] = False
            self.score += 1
        if self.runners[self.FIRST]:
            self.runners[self.FIRST] = False
            self.score += 1
        self.score += 1


batter = int(input())
hits = list(map(int, input().split()))
baseball = Baseball.play_ball()  # 初期化、スタッティクメソッドはインスタンス化しないで呼び出せる
for hit in hits:
    if hit == 1:
        baseball.single_hit()
    elif hit == 2:
        baseball.two_base_hit()
    elif hit == 3:
        baseball.three_base_hit()
    else:
        baseball.homerun()
print(baseball.score)
