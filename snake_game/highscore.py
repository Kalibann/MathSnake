from constants import PATH_HIGHSCORE


# Retornar lista de pontuações máximas
def get_high_score_list():
    try:
        with open(PATH_HIGHSCORE, "r") as arq:
            high_score = arq.readlines()
            for i, hs in enumerate(high_score):
                high_score[i] = hs.replace('\n', '')
    except FileNotFoundError:
        high_score = reset_high_score()
    return high_score


# Retornar pontuação máxima
def get_high_score():
    highscores = get_high_score_list()
    highscore = highscores[0]
    return int(highscore)


# Resetar lista de pontuações máximas
def reset_high_score():
    highscore = '0\n0\n0'
    with open(PATH_HIGHSCORE, "w") as arq:
        arq.write(highscore)
    return highscore.split('\n')


# Salvar lista de pontuações máximas
def save_high_score(new_high_score):
    high_score = get_high_score_list()
    high_score = list(map(lambda x: int(x), high_score))
    high_score.append(new_high_score)
    high_score.sort(reverse=True)

    high_score = list(map(lambda x: str(x), high_score))[0:3]

    with open(PATH_HIGHSCORE, "w") as arq:
        arq.write('\n'.join(high_score))
