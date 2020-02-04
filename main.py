"""
    *** PI ART ***
    Draws colorful points representing numbers of number PI into Archimedes spiral.
    Points are evenly spaced.
    Just change the num_points. Limit is 1000.
"""

import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos


class DrawSpiral():
    def __init__(self, arc=1, separation=1, num_points=100):
        self.arc = arc
        self.separation = separation
        self.num_points = num_points

        # defining colors for each number
        self.colors = {1: '#ff0000', 2: '#ffa500', 3: '#ffff00', 4: '#bfef45', 5: '#008000', 6: '#42d4f4', 7: '#0000ff', 8: '#4b0082', 9: '#ee82ee', 0: '#000000'}

        # points coordinates
        self.x = np.zeros(0)
        self.y = np.zeros(0)

    def points(self):
        """Returns x, y coordinates of points"""
        for value_x, value_y in self.spiral_points():
            self.x = np.append(self.x, value_x)
            self.y = np.append(self.y, value_y)
        return self.x, self.y

    def plot(self, plot_numbers = False):
        """Plots points of Archimedes spiral with given color."""
        all_values = np.array(list(self.val_from_file('pi.txt')))
        selected_values = all_values[:self.num_points + 1] # +1 is for the 3 before dot

        # plot
        fig, ax = plt.subplots()
        gVal = []
        for g in np.unique(selected_values):
            ix = np.where(selected_values == g)
            ax.scatter(self.x[ix], self.y[ix], c=self.colors[g], label=g, s=150)
            gVal.append(g)

        ax.legend()
        plt.gca().set_aspect('equal', adjustable='box')
        ax.set_title('Pi art with Archimedes spiral')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        if plot_numbers:
            for i in range(self.x.size):
                ax.annotate(i, (self.x[i], self.y[i]))

        plt.show()

    def spiral_points(self):
        """generate points on an Archimedes' spiral
        with 'arc' giving the length of arc between two points
        and 'separation' giving the distance between consecutive
        turnings
        - approximate arc length with circle arc at given distance
        - use a spiral equation r = b * phi
        """

        def p2c(r, phi):
            """polar to cartesian"""
            return (r * cos(phi), r * sin(phi))

        # yield a point at origin
        yield (0, 0)

        # initialize the next point in the required distance
        r = self.arc
        b = self.separation / (2 * pi)
        # find the first phi to satisfy distance of `arc` to the second point
        phi = float(r) / b
        num_points = self.num_points
        while num_points > 0:
            yield p2c(r, phi)
            # advance the variables
            # calculate phi that will give desired arc length at current radius
            # (approximating with circle)
            phi += float(self.arc) / r
            r = b * phi
            num_points -= 1


    def val_from_file(self, file):
        with open(file, 'r') as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                if not c == ".":
                    yield int(c)
        return c


if __name__ == '__main__':
    pi_spiral = DrawSpiral(5, 5, 767)
    pi_spiral.points()
    pi_spiral.plot(False)