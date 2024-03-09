def ft_tqdm(lst: range) -> None:
    total_iterations = len(lst)
    bar_length = 64
    for i, _ in enumerate(lst):
        progress = i / total_iterations * 100
        filled_length = int(bar_length * progress / 100)
        bar = "=" * filled_length + ">" + " " * (bar_length-filled_length-1)
        print(f"{progress:.0f}%|{bar}| {i + 1}/{total_iterations}", end="\r")
        yield i/2
