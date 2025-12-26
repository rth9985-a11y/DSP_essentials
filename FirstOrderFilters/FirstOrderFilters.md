# First Order Low-Pass/Hi-Pass Filter Theory

## Low-Pass Filter

- The LPF in this repo, "lowPassFO", is non-vectorized but does not implement real time I/O. This method writes data to an empty array of zeros and returns the filtered output
- This filter is an example of an Infinite Impulse Response (IIR) due to the recursive nature of the function. See equation below:
  $$y[n] = y[n - 1] + a(x[n] - y[n - 1])$$
  - This function, at a basic level, is a smoothing function
- The core of the function happens in the second half: $$a(x[n] - y[n - 1])$$
  - The weight, $a$ or alpha, is $0 < x <= 1$ and is calculated as such:
    $$a = \frac{2\pi fc} {2\pi fc + fs}$$
  - A higher $fc$ = $a$ closer to $1$ = more high frequencies / fast movements pass
  - When a is closer to 1 the signal is followed more closely
    - Primitavely, 1 \* input signal = input signal
- $y[n - 1]$ is the previous output
  - This is the part that makes this function recursive
  - $x[n]$ is processed relative to the previous output
- The previous outut is being added to the weighted difference between the current and previous samples!

### Use cases

- Audio
  - Filter out high frequencies
  - Avoid aliasing distortion
  - Creative audio filtering, etc...
- Sensor processing
  - Smoothing sensor signals
    - Makes them more clear
    - Results in more predictable data to analyze

## High-Pass Filter
