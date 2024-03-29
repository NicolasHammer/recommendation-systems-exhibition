"""Define utility functions used for the recommendation systems."""
from typing import List


class Accumulator:
    """For accumulating sums over some number of variables."""

    # An array of data to accumulate
    data: List[float]

    def __init__(self, n: int) -> None:
        """Initialize the data to be accumulated.

        Args:
            n: The length of the list of data to be accumulated
        """
        self.data = [0.0] * n

    def add(self, **variables_to_add) -> None:
        """Add data to the existing accumulating sums..

        variables_to_add: variables that can be converted to floats whose
            position in the argument list correspond to what element of the 
            accumulator's data array to add to.
        """
        for i, (a, b) in enumerate(zip(self.data, variables_to_add)):
            self.data[i] = a + float(b)

    def reset(self) -> None:
        """Reset the data to accumulate."""
        for i in range(len(self.data)):
            self.data[i] = 0.0

    def __getitem__(self, idx: int) -> float:
        """Get an item from the accumulator.

        Args:
            idx: The index of the item from the accumulator to get.

        Returns:
            The accumulated item at a particular index.
        """
        return self.data[idx]
