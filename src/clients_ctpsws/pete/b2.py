def bowlingScore(rolls):
    total = 0
    index = 0
    new_frame = True
    frame = 0
    for roll in rolls:
        # done when frame is 10
        if frame == 10:
            break
        # strike
        if roll == 10:
            # add next two scores
            total += rolls[index + 1]
            total += rolls[index + 2]
            # added next line to mkae it work
            frame += 1
        # 10 (not strike) add next 1 score
        elif not new_frame:
            if rolls[index - 1] + roll == 10:
                total += rolls[index + 1]
            frame += 1
            new_frame = True
        else:
            new_frame = False
        # add score and start new frame
        total += roll
        index += 1

    return total


def testBowlingScore():
    assert (bowlingScore([7, 2, 8, 2, 10, 7, 1, 8, 2, 7, 3, 10, 10, 5, 4, 8, 2, 7]) == 162)
    assert (
        bowlingScore([2, 6, 2, 6, 9, 1, 10, 10, 10, 5, 1, 4, 5, 9, 0, 9, 1, 6]) == 147
    )
    assert (
        bowlingScore([6, 4, 2, 7, 8, 1, 2, 4, 6, 3, 10, 6, 2, 1, 9, 6, 4, 10, 10, 10])
        == 137
    )
    assert bowlingScore([8, 2, 10, 10, 10, 5, 4, 10, 8, 0, 10, 10, 3, 6]) == 180
    assert bowlingScore([10] * 12) == 300


testBowlingScore()
