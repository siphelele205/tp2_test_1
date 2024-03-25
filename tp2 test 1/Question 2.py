# 2.1
def register_party(parties):
    # Define the minimum member count required for registration
    min_member_count = 5000
    
    # Check if the new party meets the criteria
    new_party = {
        "party_name": "MK party",
        "reg_number": 10003319,  # Assuming next registration number
        "member_count": 5300
    }
    
    if new_party["member_count"] >= min_member_count:
        parties.append(new_party)
        print("MK party registered successfully!")
    else:
        print("MK party does not meet the criteria for registration.")

# Example of usage
parties = [{"party_name": "Party A", "reg_number": 10003318, "member_count": 7000}]
register_party(parties)

# 2.3
def update_voter_info(voters, voter_id, name, voting_district, has_voted):
    voters[voter_id] = {"name": name, "voting_district": voting_district, "has_voted": has_voted}

# Example of usage
voters = {}
update_voter_info(voters, 1, "John Doe", "District A", False)
print(voters)

# 2.4
parties = ["ANC", "DA", "EFF", "IFP", "ATM", "COPE"]
filtered_parties = [party for party in parties if party != "COPE"]  # Assuming COPE has less than 1000 members

# Example of usage
print(filtered_parties)

# 2.5
parties = ["ANC", "DA", "EFF", "IFP", "ATM", "COPE"]
filtered_parties = list(filter(lambda party: party != "COPE", parties))

# Example of usage
print(filtered_parties)

# 2.6
voters = [
    {"name": "Alice", "registered": True},
    {"name": "Bob", "registered": False},
    {"name": "Charlie", "registered": True}
]
registered_voters = list(filter(lambda voter: voter["registered"], voters))

# Example of usage
print(registered_voters)
