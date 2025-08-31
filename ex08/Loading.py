def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_len = 25
    for i, item in enumerate(lst, 1):
        percent = int (i / total * 100)
        bar = "=" * (percent // 2) + ">" + " " * (bar_len - percent // 2)
        print(f"\r{percent}%|{bar}| {i}/{total}", end="", flush=True)
        yield item
    print()