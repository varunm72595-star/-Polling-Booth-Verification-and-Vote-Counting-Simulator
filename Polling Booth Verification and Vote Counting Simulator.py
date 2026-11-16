
from datetime import datetime
# Sample booth voter list
voters = {
    "V101": {"age": 25, "gender": "F", "voted": False, "time": None},
    "V102": {"age": 42, "gender": "M", "voted": False, "time": None},
    "V103": {"age": 31, "gender": "F", "voted": False, "time": None},
    "V104": {"age": 60, "gender": "M", "voted": False, "time": None},
    "V105": {"age": 19, "gender": "F", "voted": False, "time": None}
}
candidates = ["Candidate A", "Candidate B", "Candidate C"]
votes = {name: 0 for name in candidates}
def verify_voter(voter_id):
    if voter_id not in voters:
        print("Voter ID not found!"); return False
    if voters[voter_id]["voted"]:
        print("Duplicate voting blocked!"); return False
    print("Voter verified successfully.")
    return True
def mark_vote(voter_id):
    print("Candidates:", ", ".join(candidates))
    choice = input("Enter candidate name: ").title()
    if choice not in candidates:
        print("Invalid candidate."); return
    voters[voter_id]["voted"] = True
    voters[voter_id]["time"] = datetime.now().strftime("%H")
    votes[choice] += 1
    print("Vote recorded successfully.")
def hourly_turnout():
    total = len(voters)
    hours = {}
    for data in voters.values():
        if data["voted"]:
            hour = data["time"]
            hours[hour] = hours.get(hour, 0) + 1
    if not hours: print("No votes recorded yet.")
    for hour, count in sorted(hours.items()):
        percentage = count / total * 100
        print(f"{hour}:00 - {count} votes, {percentage:.2f}% turnout")
def declare_result():
    print("\nVote Count:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count}")
    highest = max(votes.values())
    winners = [name for name, count in votes.items() if count == highest]
    if len(winners) > 1:
        print("Result: TIE between", ", ".join(winners))
    else:
        print("Winner:", winners[0])
def main():
    print("VoteSecure - Booth Voter List Loaded")
    while True:
        print("\n1.Verify voter  2.Hourly turnout")
        print("3.Count votes/result  4.Exit")
        option = input("Choose option: ")
        if option == "1":
            voter_id = input("Enter voter ID: ").upper()
            if verify_voter(voter_id):
                confirm = input("Proceed to vote? (yes/no): ").lower()
                if confirm == "yes": mark_vote(voter_id)
        elif option == "2":
            hourly_turnout()
        elif option == "3":
            declare_result()
        elif option == "4":
            print("Polling simulation closed."); break
        else:
            print("Invalid option. Try again.")
main()
