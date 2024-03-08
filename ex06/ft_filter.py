def ft_filter(function, iterable):
    """Filters elements from an iterable based on a provided function.
    Args:
      function: A function that takes an element and returns True for
    inclusion, False otherwise.
      iterable: An iterable object (list, tuple, etc.) to be filtered.

    Returns:
      A list containing the elements from the iterable that satisfy the
    function's condition."""

    return [element for element in iterable if function(element)]
