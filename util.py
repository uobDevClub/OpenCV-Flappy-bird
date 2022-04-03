def collide_mask(leftMask, rightMask, leftRect, rightRect):
    xoffset = rightRect[0] - leftRect[0]
    yoffset = rightRect[1] - leftRect[1]
    return leftMask.overlap(rightMask, (xoffset, yoffset))