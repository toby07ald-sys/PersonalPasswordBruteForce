import hashlib

word = "dragon"
pure_hash = hashlib.sha256(word.encode()).hexdigest()

print("\n the true hash for the word " + word + " is:\n " + pure_hash + "\n")