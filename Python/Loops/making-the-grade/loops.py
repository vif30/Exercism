"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    rounded = []
    for score in student_scores:
        score = round(score)
        rounded.append(score)
    return rounded


def count_failed_students(student_scores):
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    best = []
    for score in student_scores:
        if score >= threshold:
            best.append(score)
    return best


def letter_grades(highest):
    distancia = round((highest - 40) / 4)
    qual_d = 41
    qual_c = qual_d + distancia
    qual_b = qual_c + distancia
    qual_a = qual_b + distancia
    letras = [qual_d, qual_c, qual_b, qual_a]
    return letras


def student_ranking(student_scores, student_names):
    ranking = []
    for score in range(len(student_scores)):
        student = str(score+1) + ". " + student_names[score] + ": " + str(student_scores[score])
        ranking.append(student)
    return ranking

def perfect_score(student_info):
    perfect = []
    noperfect = True
    for score in range(len(student_info)):
        if student_info[score][1] == 100:
            perfect = student_info[score]
            noperfect = False
            return perfect
    if bool(noperfect):
        return perfect
