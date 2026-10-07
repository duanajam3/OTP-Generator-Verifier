# OTP Generator & Verifier

**AVIP 2026 Cybersecurity — Task 5**

## Objective
Create an educational one-time password generator and verifier with a validity window.

## Features
- Generates a 6-digit OTP.
- Uses a secret value and current time.
- Uses HMAC-SHA256 for the OTP calculation.
- Verifies the OTP within a configurable validity window.
- Uses constant-time comparison for verification.
- Includes automated tests.

## Files
- `otp_generator.py` — main program
- `tests/test_otp_generator.py` — test cases

## How to Run

```bash
python otp_generator.py
```

Example:
```text
Enter secret: demo-secret
Generated OTP: 123456
Enter OTP to verify: 123456
Valid:
```

The exact OTP will change because it is time-based.

## How to Run Tests

```bash
python tests/test_otp_generator.py
```

Expected:
```text
All OTP tests passed.
```

## Concept
A one-time password changes over time and is intended to be used only for a limited period. This project demonstrates the basic idea of time-based verification using a shared secret.

## Security Note
This is an educational implementation, not a production authentication system. Real applications should use established, audited authentication libraries and secure secret storage.

## Ethics
Use only for learning and authorized testing of your own software.
