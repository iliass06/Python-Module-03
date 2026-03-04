if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()
    print("=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")
    alice_bob = bob.intersection(alice)
    common = charlie.intersection()
    print(f"All unique achievements: {common}")
    only_alice = alice.difference(bob.union(charlie))
    only_bob = bob.difference(alice.union(charlie))
    only_charlie = charlie.difference(bob.union(alice))
    rare = only_alice.union(only_charlie, only_bob)
    print(f"Rare achievements (1 player): {rare}")
    print()
    print(f"Alice vs Bob common: {alice_bob}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")
    