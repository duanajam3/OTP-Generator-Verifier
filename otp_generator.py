import hashlib
import hmac
import secrets
import time


def generate_event_otp(secret, digits=6):
    """Generate a one-time OTP from a secret and current time."""
    time_step = int(time.time())
    message = str(time_step).encode()
    digest = hmac.new(secret.encode(), message, hashlib.sha256).hexdigest()

    number = int(digest, 16) % (10 ** digits)
    return f"{number:0{digits}d}"


def verify_event_otp(secret, otp, validity_window=30, digits=6):
    """Verify an OTP generated within the current validity window."""
    current = int(time.time())

    for offset in range(-validity_window, validity_window + 1):
        timestamp = current + offset
        message = str(timestamp).encode()
        digest = hmac.new(secret.encode(), message, hashlib.sha256).hexdigest()
        expected = f"{int(digest, 16) % (10 ** digits):0{digits}d}"

        if hmac.compare_digest(expected, otp):
            return True

    return False


def main():
    secret = input("Enter secret: ")

    otp = generate_event_otp(secret)
    print("Generated OTP:", otp)

    entered = input("Enter OTP to verify: ")
    print("Valid:" if verify_event_otp(secret, entered) else "Invalid")


if __name__ == "__main__":
    main()
