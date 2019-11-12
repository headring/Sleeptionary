from scipy.io import wavfile

# 1초에 fs번 샘플링
fs, data = wavfile.read("0607.wav")
print(fs)
print(len(data))
