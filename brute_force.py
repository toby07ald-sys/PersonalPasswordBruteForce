import hashlib
# the target hash - this would be pulled from a leaked database in a real attack, but here we will just use the hash of 'apple' for demonstration purposes
target_hash = "14210df9e9ecbc65bd3b0a72635af4a1bbaaf06deebce89d2c1cd50854659b85"

#list of words to test the mini dictionary rather then a full dictionary attack from a text file
#dictionary_file = "test_list.txt"

#point at massive dictionary file
dictionary_file = "rockyou.txt"

print("Loading the wordlist: " + dictionary_file)
print("Starting the brute-force attack...")

#loop through each word in the wordlist, hash it, and compare it to the target hash
with open(dictionary_file, "r", encoding="latin-1") as file:
    for line in file:
        # .strip() removes the invisible return character at the end of each line
        word = line.strip()
        
        # Hash the current word
        hashed_word = hashlib.sha256(word.encode()).hexdigest()
        
        print("trying: "+ word + " -> " + hashed_word)

        # Check if it matches our target
        if hashed_word == target_hash:
            print("SUCCESS! Password found: " + word)
            break
    else:
        # This else block only triggers if the loop finishes without hitting a 'break'
        print("Failed to find the password in the wordlist.")