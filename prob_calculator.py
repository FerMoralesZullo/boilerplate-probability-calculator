import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls meet the expected criteria
        meets_criteria = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                meets_criteria = False
                break

        if meets_criteria:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability

if __name__ == '__main__':
    # Example usage
    random.seed(95)
    hat = Hat(blue=4, red=2, green=6)
    probability = experiment(
        hat=hat,
        expected_balls={"blue": 2, "red": 1},
        num_balls_drawn=4,
        num_experiments=3000
    )
    print("Probability:", probability)
