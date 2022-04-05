def collide_mask(leftMask, rightMask, leftRect, rightRect):
    xoffset = rightRect[0] - leftRect[0]
    yoffset = rightRect[1] - leftRect[1]
    return leftMask.overlap(rightMask, (xoffset, yoffset))


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)