import hashlib
# the target hash - this would be pulled from a leaked database in a real attack, but here we will just use the hash of 'apple' for demonstration purposes
targetHash = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"

#list of words to test the mini dictionary rather then a full dictionary attack from a text file
dictionary_file = "test_list.txt"

print("Loading the wordlist: " + dictionary_file)
print("Starting the brute-force attack...")

#loop through each word in the wordlist, hash it, and compare it to the target hash
with open(dictionary_file, "r", encoding="latin-1") as file:
    for line in file:
        word = line.strip()  # Remove any trailing newline characters
    #encode the word to bytes, then hash it using SHA-256, then convert to readable string
    #hash lib needs raw bytes not standard plain text to do its math 
    hashed_word = hashlib.sha256(word.encode()).hexdigest()

    print("trying: "+ word + " -> " + hashed_word)
    if hashed_word == targetHash:
        print("Password found: " + word)
        break
    else:
        # This else block only triggers if the loop finishes without hitting a 'break'
        print("Password not found in the wordlist.")