class Person:
    def __init__(self, walk_time, per_second, break_time):
        self.walk_time = walk_time
        self.per_second = per_second
        self.break_time = break_time

    def calc_dist_walked(self, time):
        if self.walk_time > (time % (self.walk_time + self.break_time)):
            time_walked = (time // (self.walk_time + self.break_time)) * self.walk_time + time % (self.walk_time + self.break_time)
        else:
            time_walked = (time // (self.walk_time + self.break_time)) * self.walk_time + self.walk_time
        dist_walked = time_walked * self.per_second
        return dist_walked


a, b, c, d, e, f, x = map(int, input().split())
takahashi = Person(a, b, c)  # インスタンス化
aoki = Person(d, e, f)
takahashi_dist = takahashi.calc_dist_walked(x)
aoki_dist = aoki.calc_dist_walked(x)

if takahashi_dist > aoki_dist:
    print("Takahashi")
elif takahashi_dist < aoki_dist:
    print("Aoki")
else:
    print("Draw")
