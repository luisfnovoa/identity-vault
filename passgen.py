import string
import secrets
import math

def calculate_entropy(password, pool_size):
    """Calculates password entropy in bits: E = L * log2(N)"""
    length = len(password)
    if length == 0 or pool_size == 0:
        return 0
    entropy = length * math.log2(pool_size)
    return round(entropy, 2)

def generate_hardened_password(length=18, use_upper=True, use_digits=True, use_special=True):
    # Base character pool (lowercase is always active)
    pool = string.ascii_lowercase
    
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_special:
        pool += string.punctuation

    # SECRETS uses the OS-level cryptographically secure pseudo-random number generator (CSPRNG)
    password = ''.join(secrets.choice(pool) for _ in range(length))
    
    # Calculate operational metrics
    entropy_bits = calculate_entropy(password, len(pool))
    
    print("\n[🔒 KRONOS IDENTITY VAULT - SECURE GENERATOR]")
    print(f"🔑 Generated Password : {password}")
    print(f"📊 Character Pool Size: {len(pool)}")
    print(f"⚡ Password Entropy   : {entropy_bits} bits")
    
    # Security diagnostics
    if entropy_bits < 60:
        print("⚠️ Status: WEAK (Easily brute-forced)")
    elif entropy_bits < 80:
        print("🛡️ Status: MODERATE (Standard protection)")
    else:
        print("💎 Status: ULTRA-SECURE (Critical Infrastructure / Crypto-resilient grade)")

if __name__ == "__main__":
    # Default execution: 18 characters with the full tactical arsenal enabled
    generate_hardened_password(length=18, use_upper=True, use_digits=True, use_special=True)