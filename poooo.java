 public static int getNextPowerOfTwo(int value) {
    int result = value;
    result -= 1;
    result |= result >> 16;
    result |= result >> 8;
    result |= result >> 4;
    result |= result >> 2;
    result |= result >> 1;
    return result + 1;
}
