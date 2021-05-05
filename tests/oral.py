import datetime


class Oral:
    """This represents the founding principles of what an oral test (a French khôlle) should be.
    This class should not be instantiated, see derived classes for actual tests.

    Tests that shall be implemented are ones which can be solved numerically (thus, proofs to theorems won't be
    asked).

    Examples of such tests:

        - Determinant computation
        - Gaussian elimination (system solving or matrix inversion)
        - Factorisation of polynomials
        - Taylor expansion calculus
        - Computation of limits
        - Gram-Schmidt orthonormalisation
        - Prime number factorisation, disjointed cycles factorisation (smaller number first)
        - Integral calculus
        - Calculus of scalar products
        - Euclidean division (integer division, polynomial division, Taylor expansion division)
        - Calculus of Bézout's coefficients
        - Modular exponentiation
        - Algebraic fraction decomposition

    """
    def __init__(self, name, time_limit, *, on_end):
        self.name = name  # The name of the test.
        self.time_limit = time_limit  # Time limit before the test is over.
        self.begin_time = 0  # A reference to when the test began.
        self.current_time = 0
        self.end_callback = on_end

    def generate(self):
        """Generates the wording of the problem. Depends on which theme it is."""
        return NotImplemented

    def check(self, user_input):
        """Checks the answer provided by the player. `user_input` may be whatever it should be, a list, a dictionary.
        This should also parse the user input, as it is up to the derived class to check whether the player entered
        bullshit."""
        return NotImplemented

    def solve(self):
        """Solves the problem beforehand. Deferred from the constructor in order not to slow down the game
        (could possibly be run in another thread)."""
        return NotImplemented

    def begin(self):
        """Begins the oral test, thus starting up the timer."""
        self.begin_time = datetime.datetime.utcnow()
        self.current_time = self.begin_time

    def update(self, delta):
        """Updates the current time. Useful to know when the test is over."""
        self.current_time += delta
        if self.current_time - self.begin_time > self.time_limit:
            self.end_callback()
