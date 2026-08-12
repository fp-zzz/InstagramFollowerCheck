def load_list(filename):
    """Load usernames from a text file, one per line"""
    with open(filename, 'r', encoding='utf-8') as f:
        # Strip whitespace and filter empty lines
        return {line.strip() for line in f if line.strip()}

def find_non_mutual(followers_file, following_file):
    """Compare followers and following lists"""
    followers = load_list(followers_file)
    following = load_list(following_file)
    
    not_following_back = following - followers  # People you follow who don't follow you
    followers_you_dont_follow = followers - following  # People who follow you but you don't
    
    return not_following_back, followers_you_dont_follow, followers, following

def main():
    # File names (adjust if yours are different)
    followers_file = "followers.txt"
    following_file = "following.txt"
    
    print("Loading lists...")
    not_following_back, followers_you_dont_follow, followers, following = find_non_mutual(
        followers_file, following_file
    )
    
    # Summary stats
    print("\n=== INSTAGRAM FOLLOWER ANALYSIS ===")
    print(f"Total followers:       {len(followers)}")
    print(f"Total following:       {len(following)}")
    print(f"Not following back:    {len(not_following_back)}")
    print(f"Follower you don't:    {len(followers_you_dont_follow)}")
    
    # Show who doesn't follow back
    if not_following_back:
        print("\n--- PEOPLE YOU FOLLOW WHO DON'T FOLLOW BACK ---")
        for username in sorted(not_following_back):
            print(f"  @{username}")
    
    # Show followers you don't follow back
    if followers_you_dont_follow:
        print("\n--- PEOPLE WHO FOLLOW YOU BUT YOU DON'T FOLLOW BACK ---")
        for username in sorted(followers_you_dont_follow):
            print(f"  {username}")

if __name__ == "__main__":
    main()