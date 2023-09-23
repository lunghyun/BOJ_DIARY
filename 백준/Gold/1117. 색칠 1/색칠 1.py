def main():
    w, h, f, c, x1, y1, x2, y2 = map(int, input().split())
    area = (x2 - x1) * (y2 - y1) * (c + 1)

    if f <= w / 2:
        if f <= x1:
            print(w * h - area)
        else:
            print(w * h - (area + (min(f, x2) - x1) * (y2 - y1) * (c + 1)))
    else:
        if w <= x1 + f:
            print(w * h - area)
        else:
            print(w * h - (area + (min(w, f + x2) - (f + x1)) * (y2 - y1) * (c + 1)))

if __name__ == "__main__":
    main()
