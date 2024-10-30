import os
import whisper

model = whisper.load_model("base")

# List all .wav files in the current directory
wav_files = [f for f in os.listdir('.') if f.endswith('.wav')]

if not wav_files:
    print("No .wav files found in the current directory.")
    exit()

# Display the list of .wav files
print("Available .wav files:")
for idx, file in enumerate(wav_files):
    print(f"{idx}: {file}")

# Select a file by index
try:
    file_index = int(input("Enter the index of the file to transcribe: "))
    if file_index < 0 or file_index >= len(wav_files):
        raise ValueError("Invalid index")
except ValueError as e:
    print(f"Error: {e}")
    exit()

filename = os.path.abspath(wav_files[file_index])

# Function to transcribe an audio file and save to text file
def transcribe_audio_file(filename, output_file="transcription.txt"):
    print(f"Transcribing audio file: {filename}")
    result = model.transcribe(filename)

    with open(output_file, "w") as file:
        file.write(result["text"])

    print(f"Transcription saved to {output_file}")

# Transcribe the audio file and save to "transcription.txt"
transcribe_audio_file(filename)