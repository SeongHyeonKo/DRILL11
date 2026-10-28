import time


class AutoRun:
    """Timed, enlarged automatic running behavior owned by a Boy instance."""

    DURATION = 5.0
    SPEED = 450.0
    SCALE = 1.6
    SCREEN_WIDTH = 800
    SPRITE_WIDTH = 100

    def __init__(self, boy):
        self.boy = boy
        self.started_at = None

    @property
    def half_width(self):
        return self.SPRITE_WIDTH * self.SCALE / 2

    def enter(self):
        self.started_at = time.monotonic()
        self.boy.frame = 0
        self.boy.frame_time = self.started_at

    def has_expired(self, now):
        return self.started_at is not None and now - self.started_at >= self.DURATION

    def update(self, now, dt):
        if self.started_at is None:
            self.enter()
            return

        if self.has_expired(now):
            self.boy.finish_auto_run()
            return

        left = self.half_width
        right = self.SCREEN_WIDTH - self.half_width
        next_x = self.boy.x + self.boy.face_dir * self.SPEED * dt

        while next_x < left or next_x > right:
            if next_x > right:
                next_x = right - (next_x - right)
                self.boy.face_dir = -1
            elif next_x < left:
                next_x = left + (left - next_x)
                self.boy.face_dir = 1
        self.boy.x = next_x

        if now - self.boy.frame_time >= self.boy.FRAME_INTERVAL:
            self.boy.frame = (self.boy.frame + 1) % 8
            self.boy.frame_time = now

    def draw(self):
        self.boy.draw_running(scale=self.SCALE, y_offset=(self.SPRITE_WIDTH * self.SCALE - self.SPRITE_WIDTH) / 2)
