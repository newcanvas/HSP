def artificial_muscle_fibers(arr: list) -> int:

    bitmap = bytearray(8192)
    repeats = 0

    for num in arr:
        num -= 1
        byte_index = num >> 2
        shift = (num & 3) << 1

        b = bitmap[byte_index]
        state = (b >> shift) & 3

        if state == 0:
            bitmap[byte_index] = b | (1 << shift)

        elif state == 1:
            repeats += 1
            bitmap[byte_index] = (b & ~(1 << shift)) | (2 << shift)

    return repeats

