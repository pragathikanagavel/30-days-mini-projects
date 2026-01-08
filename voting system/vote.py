candidates = ["A", "B", "C"]
votes = {"A": 0, "B": 0, "C": 0}
voted_users = []

while True:
    print("\nCandidates:", candidates)
    voter_id = input("Enter Voter ID (or 'exit' to finish): ")

    if voter_id.lower() == "exit":
        break

    if voter_id in voted_users:
        print("❌ You have already voted!")
        continue

    choice = input("Vote for (A/B/C): ").upper()

    if choice in candidates:
        votes[choice] += 1
        voted_users.append(voter_id)
        print("✅ Vote recorded successfully!")
    else:
        print("❌ Invalid candidate!")

print("\n--- Election Result ---")
for c in votes:
    print(c, ":", votes[c], "votes")

winner = max(votes, key=votes.get)
print("🏆 Winner:", winner)
