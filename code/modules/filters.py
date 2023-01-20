from scipy.signal import butter, sosfiltfilt
import numpy as np


def bandpass_filter(
        signal: np.ndarray,
        samplerate: float,
        lowf: float,
        highf: float,
) -> np.ndarray:
    """Bandpass filter a signal.

    Parameters
    ----------
    signal : np.ndarray
        The data to be filtered
    rate : float
        The sampling rate
    lowf : float
        The low cutoff frequency
    highf : float
        The high cutoff frequency

    Returns
    -------
    np.ndarray
        The filtered data
    """
    sos = butter(2, (lowf, highf), "bandpass", fs=samplerate, output="sos")
    filtered_signal = sosfiltfilt(sos, signal)

    return filtered_signal


def highpass_filter(
    signal: np.ndarray,
    samplerate: float,
    cutoff: float,
) -> np.ndarray:
    """Highpass filter a signal.

    Parameters
    ----------
    signal : np.ndarray
        The data to be filtered
    rate : float
        The sampling rate
    cutoff : float
        The cutoff frequency

    Returns
    -------
    np.ndarray
        The filtered data
    """
    sos = butter(2, cutoff, "highpass", fs=samplerate, output="sos")
    filtered_signal = sosfiltfilt(sos, signal)

    return filtered_signal


def lowpass_filter(
    signal: np.ndarray,
    samplerate: float,
    cutoff: float
) -> np.ndarray:
    """Lowpass filter a signal.

    Parameters
    ----------
    data : np.ndarray
        The data to be filtered
    rate : float
        The sampling rate
    cutoff : float
        The cutoff frequency

    Returns
    -------
    np.ndarray
        The filtered data
    """
    sos = butter(2, cutoff, "lowpass", fs=samplerate, output="sos")
    filtered_signal = sosfiltfilt(sos, signal)

    return filtered_signal


def envelope(signal: np.ndarray,
             samplerate: float,
             cutoff_frequency: float
             ) -> np.ndarray:
    """Calculate the envelope of a signal using a lowpass filter.

    Parameters
    ----------
    signal : np.ndarray
        The signal to calculate the envelope of
    samplingrate : float
        The sampling rate of the signal
    cutoff_frequency : float
        The cutoff frequency of the lowpass filter

    Returns
    -------
    np.ndarray
        The envelope of the signal
    """
    sos = butter(2, cutoff_frequency, "lowpass", fs=samplerate, output="sos")
    envelope = np.sqrt(2) * sosfiltfilt(sos, np.abs(signal))

    return envelope
