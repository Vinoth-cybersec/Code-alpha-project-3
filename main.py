import numpy as np
import scipy as sp


def block_RFID(signal):
    # Generate random noise with mean 0 and standard deviation 1
    noise = np.random.normal(0, 1, signal.shape)

    # Add the noise to the RFID signal to mask the tags
    masked_signal = signal + noise

    # Apply a low-pass filter to the masked signal to reduce high-frequency noise
    b, a = sp.signal.butter(10, 0.1, 'low')
    filtered_signal = sp.signal.filtfilt(b, a, masked_signal)

    # Normalize the filtered signal to ensure it falls within a reasonable range
    normalized_signal = (filtered_signal - np.min(filtered_signal)) / (
                np.max(filtered_signal) - np.min(filtered_signal))

    return normalized_signal