import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def generate_variable_star_data(
    period_days=5.0,
    amplitude=0.5,
    baseline_magnitude=12.0,
    num_points=100,
    noise_level=0.1,
    initial_phase=0,
    start_date=None,
):
    """
    Generate synthetic variable star brightness data.

    Parameters:
    -----------
    period_days : float
        Period of the variable star in days
    amplitude : float
        Amplitude of brightness variation in magnitudes
    baseline_magnitude : float
        Average magnitude of the star
    num_points : int
        Number of data points to generate
    noise_level : float
        Standard deviation of observational noise
    start_date : datetime
        Start date for observations (defaults to current date)
    initial_phase : float
        Phase offset so it does not always start at minimum

    Returns:
    --------
    pandas.DataFrame
        DataFrame with 'time' and 'brightness' columns
    """

    if start_date is None:
        start_date = datetime.now()

    # Generate time points over multiple periods
    total_days = period_days * 3  # Cover 3 periods
    time_points = np.linspace(0, total_days, num_points)

    # Generate dates
    dates = [start_date + timedelta(days=t) for t in time_points]

    # Generate periodic brightness variation (sine wave)
    phase = initial_phase + 2 * np.pi * time_points / period_days
    brightness_variation = amplitude * np.sin(phase)

    # Add some secondary variation (like a secondary star or pulsation)
    secondary_period = period_days * 0.3
    secondary_phase = 2 * np.pi * time_points / secondary_period
    secondary_variation = 0.1 * amplitude * np.sin(secondary_phase)

    # Combine variations
    total_variation = brightness_variation + secondary_variation

    # Add observational noise
    noise = np.random.normal(0, noise_level, num_points)

    # Calculate final brightness (brighter = lower magnitude)
    brightness = baseline_magnitude - total_variation + noise

    # Create DataFrame
    data = pd.DataFrame({"time": dates, "brightness": brightness})

    return data


def plot_light_curve(data, save_plot=False):
    """
    Plot the light curve and optionally save it.

    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame with 'time' and 'brightness' columns
    save_plot : bool
        Whether to save the plot as PNG
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data["time"], data["brightness"], "o-", alpha=0.7, markersize=4)
    plt.xlabel("Time")
    plt.ylabel("Magnitude (brighter = lower)")
    plt.title("Synthetic Variable Star Light Curve")
    plt.grid(True, alpha=0.3)
    plt.gca().invert_yaxis()  # Invert y-axis so brighter is up

    if save_plot:
        plt.savefig("variable_star_light_curve.png", dpi=300, bbox_inches="tight")
        print("Light curve plot saved as 'variable_star_light_curve.png'")

    plt.show()


def main():
    """Main function to generate and save variable star data."""

    print("Generating synthetic variable star brightness data...")

    # Generate data with realistic parameters
    data = generate_variable_star_data(
        period_days=100,
        amplitude=1,
        baseline_magnitude=-2,
        num_points=150,
        noise_level=0.5,
        start_date=datetime(2024, 1, 1),
        initial_phase=np.pi * 1.89,
    )

    # Save to CSV
    csv_filename = "06_functions/data/star3.csv"
    data.to_csv(csv_filename, index=False)
    print(f"Data saved to '{csv_filename}'")
    print(f"Generated {len(data)} data points")
    print(f"Time range: {data['time'].min()} to {data['time'].max()}")
    print(
        f"Brightness range: {data['brightness'].min():.3f} to {data['brightness'].max():.3f} magnitudes"
    )

    # Display first few rows
    print("\nFirst 10 data points:")
    print(data.head(10))

    # Create and save plot
    # plot_light_curve(data)

    return data


if __name__ == "__main__":
    data = main()
