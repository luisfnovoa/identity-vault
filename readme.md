Identity Vault: Secure Hardened Password Generator

Overview

Identity Vault is a high-security password generator engineered for critical environments. It leverages Python's secrets module, utilizing the operating system's cryptographically secure pseudo-random number generator (CSPRNG) to ensure maximum entropy and resilience against brute-force attacks.

Technical Specifications

Native CSPRNG: Generation powered by the secrets module for cryptographic integrity.

Real-time Entropy Calculation: 

Automatic measurement of password complexity (in bits).

Security Diagnostics: Immediate classification of protection levels:

WEAK: $< 60$ bits.

MODERATE: $60-80$ bits.

ULTRA-SECURE: $> 80$ bits.

🚀 Usage

<img width="730" height="116" alt="Captura de pantalla 2026-06-08 203459" src="https://github.com/user-attachments/assets/20e1ee43-247e-4833-9e1d-69b5fef47665" />

