import numpy as np

def mean_squared_error(y_true, y_pred):
    """
    Calculate the Mean Squared Error (MSE) between actual and predicted values.

    Parameters:
    y_true (array-like): Array of actual values
    y_pred (array-like): Array of predicted values

    Returns:
    float: The Mean Squared Error
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # Ensure input arrays are of the same shape
    if y_true.shape != y_pred.shape:
        raise ValueError("Shapes of y_true and y_pred must match.")

    # Calculate MSE
    mse = np.mean((y_true - y_pred) ** 2)
    return mse

# Example usage
if __name__ == "__main__":
    # Take input from the user
    actual = list(map(float, input("Enter actual values separated by spaces: ").split()))
    predicted = list(map(float, input("Enter predicted values separated by spaces: ").split()))

    # Compute MSE
    try:
        mse_value = mean_squared_error(actual, predicted)
        print(f"Mean Squared Error: {mse_value}")
    except ValueError as e:
        print(e)
