import soundfile as sf
from normalizer import norm
from FirstOrderFilters.lowPassFO import lpfFO
from FirstOrderFilters.highPassFO import hpfFO

file = input("Enter file path: ")
data, fs = sf.read(file)
command = input("Choose a process ('ls' to list all proceses: ")

# 'ls' handling
if command == "ls":
    print("FOLPF - First Order Low-Pass Filter\n" \
            "FOHPF - First Order Hi-Pass Filter\n" \
            "D - Delay\n" \
            "SH - Shift By x Miliseconds\n" \
            "SC - Soft Clip")

# First order low pass filter    
if command == "FOLPF":

    fc = input("Frequency Cutoff (fc): ")

    norm = norm()
    lpf = lpfFO(fs, norm, fc)
    output = lpf.process(data)

    # write to sound file

if command == "FOHPF":

    fc = input("Frequency Cutoff (fc)")

    norm = norm()
    hpf = hpfFO(fs, norm, fc)
    output = hpf.process(data)

    # write to sound file


