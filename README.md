# MeanSquareFunction

# README Section
"""
# Mean Squared Error (MSE) Implementation

This script provides an implementation of the Mean Squared Error (MSE) loss function, a widely used metric to evaluate machine learning regression models. It calculates the average squared difference between actual and predicted values.

## Why MSE Matters
MSE is critical for model evaluation because it:
- Penalizes larger errors more than smaller ones due to squaring.
- Provides a single scalar value summarizing model performance.
- Highlights how well the model's predictions align with actual outcomes.

## Usage
### Example Scenario
Imagine you are building a predictive model to forecast house prices. After training your model, you obtain the following values:

- Actual prices: `[3.0, -0.5, 2.0, 7.0]`
- Predicted prices: `[2.5, 0.0, 2.1, 7.8]`

By using the `mean_squared_error` function in this script, you can calculate how close the predictions are to the actual values.

```python
# Example code
actual = [3.0, -0.5, 2.0, 7.0]
predicted = [2.5, 0.0, 2.1, 7.8]

mse_value = mean_squared_error(actual, predicted)
print(f"Mean Squared Error: {mse_value}")
```

### Interactive Input
You can also provide input interactively:

```python
Enter actual values separated by spaces: 3.0 -0.5 2.0 7.0
Enter predicted values separated by spaces: 2.5 0.0 2.1 7.8
Mean Squared Error: 0.3725
```

## Dependencies
- `numpy`: Install using `pip install numpy`

## Error Handling
The function ensures that the shapes of the actual and predicted arrays match. If not, it raises a `ValueError`.

## Conclusion
This implementation of MSE is simple and flexible, making it ideal for evaluating regression models in various scenarios. Modify or integrate it into your projects as needed!
"""
