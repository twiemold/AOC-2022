import enum

DRAW_POINTS = 3
WIN_POINTS = 6


class ScoreEnums(enum.IntEnum):
    ROCK_SCORE = 1
    PAPER_SCORE = 2
    SCISSORS_SCORE = 3


class ElfEnums(enum.Enum):
    ROCK_PLAY = 'A'
    PAPER_PLAY = 'B'
    SCISSORS_PLAY = 'C'


class SantaEnums(enum.Enum):
    ROCK_PLAY = 'X'
    PAPER_PLAY = 'Y'
    SCISSORS_PLAY = 'Z'


class OutcomeEnums(enum.Enum):
    MUST_LOSE = 'X'
    MUST_DRAW = 'Y'
    MUST_WIN = 'Z'


def read_file(filename: str) -> list[str]:
    data = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            data.append(line)
    return data


def create_matched_list(data: list[str]) -> list[list[str]]:
    play_list = []
    for line in data:
        sub_list = []
        plays = line.split(' ')
        sub_list.append(plays[0])
        sub_list.append(plays[1].strip())
        play_list.append(sub_list)
    return play_list


def return_needed_outcome(elf_play: str, needed_outcome: str) -> int:
    if needed_outcome == OutcomeEnums.MUST_LOSE.value:
        if elf_play == ElfEnums.ROCK_PLAY.value:
            return ScoreEnums.SCISSORS_SCORE.value
        elif elf_play == ElfEnums.PAPER_PLAY.value:
            return ScoreEnums.ROCK_SCORE.value
        else:
            return ScoreEnums.PAPER_SCORE.value
    elif needed_outcome == OutcomeEnums.MUST_DRAW.value:
        if elf_play == ElfEnums.ROCK_PLAY.value:
            return ScoreEnums.ROCK_SCORE.value + DRAW_POINTS
        elif elf_play == ElfEnums.PAPER_PLAY.value:
            return ScoreEnums.PAPER_SCORE.value + DRAW_POINTS
        else:
            return ScoreEnums.SCISSORS_SCORE.value + DRAW_POINTS
    else:
        if elf_play == ElfEnums.ROCK_PLAY.value:
            return ScoreEnums.PAPER_SCORE.value + WIN_POINTS
        elif elf_play == ElfEnums.PAPER_PLAY.value:
            return ScoreEnums.SCISSORS_SCORE.value + WIN_POINTS
        else:
            return ScoreEnums.ROCK_SCORE.value + WIN_POINTS


def calculate_score(play_list: list[list[str]]) -> int:
    score = 0
    for plays in play_list:
        score += return_needed_outcome(plays[0], plays[1])
    return score


def test():
    test_plays = [
        ['A', 'Y'],
        ['B', 'X'],
        ['C', 'Z']
    ]
    score = calculate_score(test_plays)
    assert score == 12


def main():
    test()
    data = read_file('input.txt')
    play_list = create_matched_list(data)
    score = calculate_score(play_list)
    print(f'Your score will be {score}')


if __name__ == '__main__':
    main()
