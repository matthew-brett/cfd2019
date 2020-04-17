The [reverse probability page](first_bayes) has a game, that we analyzed by simulation, and then by reflection.

The game is:

* I have two boxes; *box4* with 4 red balls and 1 green ball, and *box2* with
  two red balls and three green balls.
* I offer you one of these two boxes at random, without telling you which.
* You draw a ball at random from the box, and you get a red ball.
* What is the probability that I gave you box4?

We found by simulation, and later by reflection, that the probability is 0.67.

The logic we discovered was:

* We want the proportion of "red" trials that came from box4.
* Calculate the proportion of trials that are *both* box4 and red, and divide
  by the overall proportion of red trials.

We found the proportion of red trials that are *both* box4 *and* red is the
proportion of box4 trials multiplied by (the proportion of box4 trials that
are red.

This logic above is a fundamental rule in probability called [Bayes
theorem](https://en.wikipedia.org/wiki/Bayes'_theorem).

In this page, we relate the logic above to the usual way of describing Bayes
theorem.

First we need some notation.

The probability that I give you *box4* on any one trial is 0.5.

I write this as:

$$
P(box4) = 0.5
$$

Read this as "the probability of *box4* is 0.5".

Similarly:

$$
P(box2) = 0.5
$$

The probability of getting a red ball, given that I am drawing from *box4*, is 4/5 = 0.8.  We write "given" here with the bar: $\mid$.

$$
P(red \mid box4) = 0.8
$$

Read this as "the probability of drawing a red ball given I have box4 is 0.8".

Similarly:

$$
P(red \mid box2) = 0.4
$$

We follow the logic above, with this notation.  Here is the logic again:

1. We want the proportion of "red" trials that came from box4.
2. Calculate the proportion of trials that are *both* box4 and red, and divide
   by the overall proportion of red trials.

We can express the first statement by saying that we are trying to find
$P(box4 \mid red)$.

Therefore, the second statement says:

$$
P(box4 \mid red) = \frac{P(box4 \cap red)}{P(red)}
$$

Remember from the [reverse probability page](first_bayes) that we found
$P(red)$ by adding the probabilities of the two different ways we can get
a red ball: $P(red) = P(red | box4) + P(red | box2)$.

Putting the first and second statements together into one, we get:

$$
P(box4 \mid red) = \frac{P(box4) P(red \mid box4)}{P(red)}
$$

This is Bayes theorem, although it is usually written with the multiplication in the other order:

$$
P(box4 \mid red) = \frac{P(red \mid box4) P(box4)}{P(red)}
$$