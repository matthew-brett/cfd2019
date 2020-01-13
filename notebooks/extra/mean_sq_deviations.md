## The mean and squared differences

This page is assumes a lot more maths than the standard bit of the course.  In
particular, it assumes that that you know the basics of finding the
[derivative](https://en.wikipedia.org/wiki/Derivative) of a function.

In practice, if you're in the US, you will need late high-school mathematics,
and if you're in the UK, that means you will need A-level maths.

Nothing in the rest of the course assumes you can follow the mathematics in this page.  The page is just for those of you who are interested, and do know that part of mathematics.

In [the meaning of the mean](../08/mean_meaning) we were studying prediction
errors.

We imagined using the mean of a set of value as a predictor for those values.  Then we looked at how far off we would be, on average, if we use the mean to predict each value.

Let's say we have a sequence of $n$ values.  For example, $n$ could be 8.  Call
the first value $x_1$, the second $x_2$ and so on, up to $x_n$.  For example,
if $n = 8$, then the sequence of eight values would be ${x_1, x_2, x_3, x_4,
x_5, x_6, x_7, x_8}$.  In general I can write the sequence of $n$ values as
${x_1, x_2, ..., x_n}$.

We often want to add up all the values, for example, when we calculate the
mean.  I could write $x_1 + x_2 + ... + x_n$, but that is rather long and
clumsy.  The mathematical shorthand for this is $\sum x_i$, meaning add up all
the values in the sequence ${x_1, x_2, ..., x_n}$.

We can write the mean using this notation.  Use the symbol $\bar{x}$ to refer
to the mean of the sequence ${x_1, x_2, ... x_n}$. Then the definition of the mean is:

$$
\bar{x} = \frac{1}{n}\sum x_i
$$

Now we have the notation, we can return to our problem.

We are to going to take some value $c$, and subtract it from all the values in
${x_1, x_2, ... x_n}$.  This will give us a new sequence of *deviations* or
*errors* ${x_1 - c, x_1 - c, ..., x_n - c}$.  Then we will square the
errors, to get ${(x_1 - c)^2, (x_2 - c)^2, ... (x_n - c)^2}$, and finally
we will add all up all these squared errors: $\sum (x_i - c)^2$.  Call this,
the Sum of Squared Errors or $SSE$ for a particular value $c$.  So:

$$
\begin{equation}
SSE_c = \sum (x_i - c)^2 \tag{SSE_c}\label{eq:sse_c}
\end{equation}
$$

This is the general formula for the plot we saw at the end of [the meaning of
the mean page](../08/mean_meaning), where the value for $c$ is on the horizontal axis, and the value for $SSE_c$ is on the vertical axis.

Specifically, we want to find the value of $c$ that gives the smallest value for $SSE_c$.

The plot turned out to be U-shaped, where we want to find the horixontal axis location corresponding to the bottom of the U.

We can find this location by transforming the formula equation \eqref{eq:sse_c} above
into a formula for the *gradient* of the line that the formula represents.
This is *taking the derivative*.  When the *derivative* of equation \eqref{eq:sse_c} is
equal to zero, it means the *gradient* of equation \eqref{eq:sse_c} is 0, and this is
true when we are at a peak or a trough of the original equation \eqref{eq:sse_c}
formula.  We want the trough.

Let's start by expanding out equation \eqref{eq:sse_c}, and using the [laws of sums](http://matthew-brett.github.io/teaching/some_sums.html) to simplify the result:

$$
SSE_c = \sum (x_i - c)^2 \implies \\
= \sum (x_i^2 - 2 x_i c + c^2) \implies \\
= \sum x_i^2 - 2 c \sum x_i + n c^2
$$

Now differentiate with respect to $c$:

$$
\begin{equation}
\frac{\partial SSE_c}{\partial c} = -2 \sum x_i + 2 n c \tag{dSSE_c}\label{eq:dsse_c}
\end{equation}
$$

When equation \eqref{eq:dsse_c} has value zero, we can be at a peak (the
gradient is zero, but it's about to become negative) or a trough (the gradient
is zero, but it's about to become positive).

Find the zero(s) for equation \eqref{eq:dsse_c}:

$$
2 \sum x_i = 2 n c \implies \\
\frac{1}{n} \sum x_i = c
$$

Equation \eqref{eq:dsse_c} only has one zero, and it is when $c$ is equal to
the mean.

We so far don't know if this is a peak or a trough, but we can differentiate
equation \eqref{eq:dsse_c} again, to see the slope of the slope.  If this is
positive at $c = \frac{1}{n} \sum x_i$, than the slope is changing to be
positive, and we would be at a trough, if it is negative, the slope is changing
to be negative, and we would be at a peak.  Here's the derivative of equation
\eqref{eq:dsse_c}, also called the [second
derivative](https://en.wikipedia.org/wiki/Second_derivative):

$$
\frac{\partial ^2SSE_c}{\partial c^2} = 2 n
$$

$n$ is always positive; this means that the second derivative is always
positive, and therefore, it is also positive at our zero point $c = \frac{1}{n}
\sum x_i$.  So, equation \eqref{eq:sse_c} only has a one trough, at $c =
\frac{1}{n} \sum x_i$, and no peaks.

Therefore the mean $\frac{1}{n}\sum x_i$ is the value $c$ that minimizes the
sum of squared errors, also called the sum of squared deviations, also called
the sum of squared prediction errors.
