lessons = {}


def get_sum(*args):
    time = 0
    for arg in args:
        time += 0 if arg == '—' or arg == '—\n' else int(arg.split('(', 1)[0])
    return time


try:
    for line in open("task_6.txt", encoding='utf-8'):
        lesson_name, lecture, practice, lab = line.split('   ')
        lessons[lesson_name[:-1]] = get_sum(lecture, practice, lab)
except IOError:
    print("Файла не существует!")

print(lessons)
