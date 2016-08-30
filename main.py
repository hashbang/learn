def play_lessons():
    with open('lessons.txt') as lessons:
        next(lessons)
        for lesson in lessons:
            les = 'lessons.' + lesson.rstrip()
            l = __import__(les, fromlist=['start'])
            l.start()


if __name__ == "__main__":
    #main game loop executes
    play_lessons()