import hashlib
# the target hash - this would be pulled from a leaked database in a real attack, but here we will just use the hash of 'apple' for demonstration purposes
target_hash = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"

#list of words to test the mini dictionary rather then a full dictionary attack from a text file
dictionary_file = "test_list.txt"

print("Loading the wordlist: " + dictionary_file)
print("Starting the brute-force attack...")

#loop through each word in the wordlist, hash it, and compare it to the target hash
with open(dictionary_file, "r", encoding="latin-1") as file:
    for line in file:
        # .strip() removes the invisible return character at the end of each line
        word = line.strip()
        
        # Hash the current word
        hashed_word = hashlib.sha256(word.encode()).hexdigest()
        
        # Check if it matches our target
        if hashed_word == target_hash:
            print("SUCCESS! Password found: " + word)
            break
    else:
        # This else block only triggers if the loop finishes without hitting a 'break'
        print("Failed to find the password in the wordlist.")